# -*- coding: utf-8 -*- 
# @Time : 2020/5/7 17:33 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : pool.py 
# @Software: PyCharm

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=2)
    res = pool.map(job, range(10))
    print(res)

    res = pool.apply_async(job, (2,))
    print(res.get())

    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()