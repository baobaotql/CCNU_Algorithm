# -*- coding: utf-8 -*- 
# @Time : 2019/10/10 21:29 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : binary.py 
# @Software: PyCharm

#recursion
def recursion(n):
    result = ''
    if n == 0:
        return result
    else:
        result = recursion(n//2)
        return result + str(n%2)

num_a = int(input("input a decimal number : "))

if num_a >= 90000:
    print("error！")
else:
    print(recursion(num_a))



#non-recursion

def non_recursion(n):
    s = ''
    while n > 0:
        s = str(n%2) + s    # 取余后更新 s
        n = n//2            # 取整后更新 n
    return s
num_b = int(input("input another decimal number : "))

if num_b >= 90000:
    print("error!")
else:
    print(non_recursion(num_b))
