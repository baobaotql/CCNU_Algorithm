# -*- coding: utf-8 -*- 
# @Time : 2020/5/7 16:33 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : queue_test.py 
# @Software: PyCharm
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000):
        res += i + i**2+ i**3
    q.put(res)

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    res1 = q.get()
    res2 = q.get()

    print(res1)
    print(res2)

    print(res1 + res2)
