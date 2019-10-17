# -*- coding: utf-8 -*- 
# @Time : 2019/10/11 0:25 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : Fibonacci.py 
# @Software: PyCharm
import time

#recursion
def fib_recursion(n):
    if  n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

num_a = int(input("input a number : "))
tic = time.process_time()
if num_a==0:
    print("error!")
else:
    print(fib_recursion(num_a))
    toc = time.process_time()
    print("time : "+ str(1000*(toc-tic)))



#non_recursion
def fib_loop(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a

num_b = int(input("input a number : "))
tic = time.process_time()
if num_b==0:
    print("error!")
else:
    print(fib_loop(num_b))
    toc = time.process_time()
    print("time : " + str(1000 * (toc - tic)))



#another method
class Fibonacci(object):
    '''
    斐波那契数列迭代器
    '''
    def __init__(self,n):
        '''

        :param n: int 指的是生成数列的个数
        '''
        self.n = n
        #保存当前生成的数列的第几个数据 生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        '''

        :return:当前使用next()函数调用时，就会获取下一个数
        '''
        if self.current<self.n:
            self.a,self.b = self.b,self.a+self.b
            self.current +=1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        '''

        :return: 迭代器的__iter__返回自身即可
        '''
        return self

if __name__ == '__main__':
    num_c = int(input("input a number : "))
    fib = Fibonacci(num_c)
    for n in fib:
        print(n)
