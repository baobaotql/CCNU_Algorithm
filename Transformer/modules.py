# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 11:12
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : modules.py 
# @Software: PyCharm
import tensorflow as tf
import numpy as np

def embedding(inputs,
              vocab_size,
              num_units,
              zero_pad=True,
              scale=True,
              scope="embedding",
              reuse=None):

    with tf.variable_scope(scope, reuse=reuse):
        lookup_table = tf.get_variable('lookup_table',
                                       dtype=tf.float32,
                                       shape=[vocab_size, num_units],
                                       initializer=tf.contrib.layers.xavier_initializer())
        if zero_pad:
            lookup_table = tf.concat((tf.zeros(shape=[1, num_units]),
                                      lookup_table[1:, :]), 0)
        outputs = tf.nn.embedding_lookup(lookup_table, inputs)

        if scale:
            outputs = outputs * (num_units ** 0.5)

    return outputs


def positional_encoding(inputs,
                        num_units,
                        zero_pad = True,
                        scale = True,
                        scope = "positional_encoding",
                        reuse=None):

    N,T = inputs.get_shape().as_list()
    with tf.variable_scope(scope,reuse=True):
        position_ind = tf.tile(tf.expand_dims(tf.range(T),0),[N,1])

        position_enc = np.array([
            [pos / np.power(10000, 2.*i / num_units) for i in range(num_units)]
            for pos in range(T)])

        position_enc[:,0::2] = np.sin(position_enc[:,0::2]) # dim 2i
        position_enc[:,1::2] = np.cos(position_enc[:,1::2]) # dim 2i+1

        lookup_table = tf.convert_to_tensor(position_enc)

        if zero_pad:
            lookup_table = tf.concat((tf.zeros(shape=[1,num_units]),lookup_table[1:,:]),0)

        outputs = tf.nn.embedding_lookup(lookup_table,position_ind)

        if scale:
            outputs = outputs * num_units ** 0.5

        return outputs


def multihead_attention(queries,keys,num_units=None,
                        num_heads = 0,
                        dropout_rate = 0,
                        is_training = True,
                        causality = False,
                        scope = "mulithead_attention",
                        reuse = None):

    with tf.variable_scope(scope,reuse=reuse):
        if num_units is None:
            num_units = queries.get_shape().as_list[-1]

        # Linear projection
        Q = tf.layers.dense(queries,num_units,activation=tf.nn.relu) #
        K = tf.layers.dense(keys,num_units,activation=tf.nn.relu) #
        V = tf.layers.dense(keys,num_units,activation=tf.nn.relu) #

        # Split and Concat
        Q_ = tf.concat(tf.split(Q,num_heads,axis=2),axis=0) #
        K_ = tf.concat(tf.split(K,num_heads,axis=2),axis=0)
        V_ = tf.concat(tf.split(V,num_heads,axis=2),axis=0)

        outputs = tf.matmul(Q_,tf.transpose(K_,[0,2,1]))
        outputs = outputs / (K_.get_shape().as_list()[-1] ** 0.5)

        # 这里是对填充的部分进行一个mask，这些位置的attention score变为极小，我们的embedding操作中是有一个padding操作的，
        # 填充的部分其embedding都是0，加起来也是0，我们就会填充一个很小的数。
        key_masks = tf.sign(tf.abs(tf.reduce_sum(keys,axis=-1)))
        key_masks = tf.tile(key_masks,[num_heads,1])
        key_masks = tf.tile(tf.expand_dims(key_masks,1),[1,tf.shape(queries)[1],1])

        paddings = tf.ones_like(outputs) * (-2 ** 32 + 1)
        outputs = tf.where(tf.equal(key_masks,0),paddings,outputs)

        # 这里其实就是进行一个mask操作，不给模型看到未来的信息。
        if causality:
            diag_vals = tf.ones_like(outputs[0,:,:])
            # tril = tf.linalg.LinearOperatorLowerTriangular(diag_vals).to_dense()
            # tril = tf.contrib.linalg.LinearOperatorTriL(diag_vals).to_dense()
            tril = tf.linalg.LinearOperatorLowerTriangular(diag_vals).to_dense()
            masks = tf.tile(tf.expand_dims(tril,0),[tf.shape(outputs)[0],1,1])

            paddings = tf.ones_like(masks) * (-2 ** 32 + 1)
            outputs = tf.where(tf.equal(masks,0),paddings,outputs)

        outputs = tf.nn.softmax(outputs)

        # Query Mask
        query_masks = tf.sign(tf.abs(tf.reduce_sum(queries,axis=-1)))
        query_masks = tf.tile(query_masks,[num_heads,1])
        query_masks = tf.tile(tf.expand_dims(query_masks,-1),[1,1,tf.shape(keys)[1]])
        outputs *= query_masks

        # Dropout
        outputs = tf.layers.dropout(outputs,rate = dropout_rate,training = tf.convert_to_tensor(is_training))

        # Weighted sum
        outputs = tf.matmul(outputs,V_)

        # restore shape
        outputs = tf.concat(tf.split(outputs,num_heads,axis=0),axis=2)

        # Residual connection
        outputs += queries

        # Normalize
        outputs = normalize(outputs)

    return outputs



def normalize(inputs,
              epsilon=1e-8,
              scope="ln",
              reuse=None):

    with tf.variable_scope(scope, reuse=reuse):
        inputs_shape = inputs.get_shape()
        params_shape = inputs_shape[-1:]

        mean, variance = tf.nn.moments(inputs, [-1], keep_dims=True)
        beta = tf.Variable(tf.zeros(params_shape))
        gamma = tf.Variable(tf.ones(params_shape))
        normalized = (inputs - mean) / ((variance + epsilon) ** (.5))
        outputs = gamma * normalized + beta

    return outputs

def feedforward(inputs,
                num_units=[2048, 512],
                scope="multihead_attention",
                reuse=None):

    with tf.variable_scope(scope, reuse=reuse):
        # Inner layer
        params = {"inputs": inputs, "filters": num_units[0], "kernel_size": 1,
                  "activation": tf.nn.relu, "use_bias": True}
        outputs = tf.layers.conv1d(**params)

        # Readout layer
        params = {"inputs": outputs, "filters": num_units[1], "kernel_size": 1,
                  "activation": None, "use_bias": True}
        outputs = tf.layers.conv1d(**params)

        # Residual connection
        outputs += inputs

        # Normalize
        outputs = normalize(outputs)

    return outputs


def label_smoothing(inputs, epsilon=0.1):
    K = inputs.get_shape().as_list()[-1]  # number of channels
    return ((1 - epsilon) * inputs) + (epsilon / K)


def scaled_dotproduct_attention(queries,keys,num_units=None,
                        num_heads = 0,
                        dropout_rate = 0,
                        is_training = True,
                        causality = False,
                        scope = "mulithead_attention",
                        reuse = None):

    with tf.variable_scope(scope,reuse=reuse):
        if num_units is None:
            num_units = queries.get_shape().as_list[-1]

        # Linear projection
        Q = tf.layers.dense(queries,num_units,activation=tf.nn.relu) #
        K = tf.layers.dense(keys,num_units,activation=tf.nn.relu) #
        V = tf.layers.dense(keys,num_units,activation=tf.nn.relu) #

        outputs = tf.matmul(Q,tf.transpose(K,[0,2,1]))
        outputs = outputs / (K.get_shape().as_list()[-1] ** 0.5)

        # 这里是对填充的部分进行一个mask，这些位置的attention score变为极小，我们的embedding操作中是有一个padding操作的，
        # 填充的部分其embedding都是0，加起来也是0，我们就会填充一个很小的数。
        key_masks = tf.sign(tf.abs(tf.reduce_sum(keys,axis=-1)))
        key_masks = tf.tile(tf.expand_dims(key_masks,1),[1,tf.shape(queries)[1],1])

        paddings = tf.ones_like(outputs) * (-2 ** 32 + 1)
        outputs = tf.where(tf.equal(key_masks,0),paddings,outputs)

        # 这里其实就是进行一个mask操作，不给模型看到未来的信息。
        if causality:
            diag_vals = tf.ones_like(outputs[0,:,:])
            tril = tf.contrib.linalg.LinearOperatorTriL(diag_vals).to_dense()
            masks = tf.tile(tf.expand_dims(tril,0),[tf.shape(outputs)[0],1,1])

            paddings = tf.ones_like(masks) * (-2 ** 32 + 1)
            outputs = tf.where(tf.equal(masks,0),paddings,outputs)

        outputs = tf.nn.softmax(outputs)

        # Query Mask
        query_masks = tf.sign(tf.abs(tf.reduce_sum(queries,axis=-1)))
        query_masks = tf.tile(tf.expand_dims(query_masks,-1),[1,1,tf.shape(keys)[1]])
        outputs *= query_masks

        # Dropout
        outputs = tf.layers.dropout(outputs,rate = dropout_rate,training = tf.convert_to_tensor(is_training))

        # Weighted sum
        outputs = tf.matmul(outputs,V)

        # Residual connection
        outputs += queries

        # Normalize
        outputs = normalize(outputs)

    return outputs