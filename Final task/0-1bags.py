# -*- coding: utf-8 -*- 
# @Time : 2019/12/15 16:30 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : 0-1bags.py 
# @Software: PyCharm
def bag(n, c, w, v):
	value = [[0 for j in range(c + 1)] for i in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, c + 1):
			if j < w[i - 1]:
				value[i][j] = value[i - 1][j]
			else:
				value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])# 背包总容量够放当前物体，取最大价值
	return value

def show(n, c, w, value):
    x = [0 for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = 1
            j -= w[i - 1]

    print('背包中所装物品为:')
    weight = 0
    for i in range(n):
        if x[i]:
            print('第', i+1, '个 ', end='')
            print('重量为', w[i], ' ', end='')
            print('价值为', v[i], ' ', end='\n')
            weight = weight + w[i]

    print('最大价值为:', value[n][c])
    print('背包重量为：', weight)


if __name__=='__main__':
    n = 20
    c = 878
    w = []
    v = []

    '''
    weight_i = [92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58]
	value_j = [44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63]
    '''

    for i in range(0, n):
        print('第', i + 1, '件物品重量:')
        weight_i = int(input())
        w.append(weight_i)

    print("/******************************/")

    for j in range(0, n):
        print('第', j + 1, '件物品价格:')
        value_j = int(input())
        v.append(value_j)

    print('所有商品重量：',w)
    print('所有商品价格：', v)

    value = bag(n, c, w, v)
    show(n, c, w, value)
