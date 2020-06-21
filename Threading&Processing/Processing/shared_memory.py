# -*- coding: utf-8 -*- 
# @Time : 2020/5/7 18:53 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : shared_memory.py 
# @Software: PyCharm

import multiprocessing as mp

value1 = mp.Value('i', 0)
value2 = mp.Value('d', 3.14)

array = mp.Array('i', [1,2,3])