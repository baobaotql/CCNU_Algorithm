# -*- coding: utf-8 -*- 
# @Time : 2019/12/15 18:00 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : Integer_partition.py 
# @Software: PyCharm

def partition(n, m, string):
    if n == 0:
        print(string)
    else:
        if m > 1:
            partition(n, m - 1, string)
        if m <= n:
            partition(n - m, m, str(m) + ' ' + string)


def divide(n, m):
    if (n == 1) or (m == 1):
        return 1
    if n < m:
        return divide(n, n)
    if n == m:
        return divide(n, n-1) + 1
    if n > m > 1:
        return divide(n, m-1) + divide(n-m, m)

if __name__ == '__main__':
    print('输入一个整数：')
    n = int(input())
    m = n
    p = divide(n, m)
    print('划分方法有%d种' % p)
    print('%d的划分如下：' % n)
    partition(n, m, '')
