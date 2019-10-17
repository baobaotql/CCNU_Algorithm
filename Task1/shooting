# -*- coding: utf-8 -*- 
# @Time : 2019/10/12 11:29 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : shooting.py 
# @Software: PyCharm

times = 0
def shooting(n,sum):
    global  times
    if n<0:
        return
    elif (45 - sum)>(10*(n)):
        return
    elif (sum == 45) and (n == 0):
        times += 1
        return
    for i in range(11):
        shooting(n - 1,sum + i)

shooting(6,0)


print('there are %d possibilities'%times)
