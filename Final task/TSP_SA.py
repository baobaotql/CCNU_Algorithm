# -*- coding: utf-8 -*- 
# @Time : 2019/12/16 11:32 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : TSP_SA.py 
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import imageio
import pdb

"旅行商问题 ( TSP , Traveling Salesman Problem )"
coordinates = np.array([
	[41, 94],
    [37, 84],
    [54, 67],
    [25, 62],
    [7, 64],
    [2, 99],
    [68, 58],
    [71, 44],
    [54, 62],
    [83, 69],
    [64, 60],
    [18, 54],
    [22, 60],
    [83, 46],
    [91, 38],
    [25, 38],
    [24, 42],
    [58, 69],
    [71, 71],
    [74, 78],
    [87, 76],
    [18, 40],
    [13, 40],
    [82, 7],
    [62, 32],
    [58, 35],
    [45, 21],
    [41, 26],
    [44, 35],
    [4, 50]])


# 得到距离矩阵的函数
def getdistmat(coordinates):
	'''

	:param coordinates:
	:return:
	'''
	num = coordinates.shape[0]  # 30个坐标点
	distmat = np.zeros((30, 30))  # 30X30距离矩阵
	for i in range(num):
		for j in range(i, num):
			distmat[i][j] = distmat[j][i] = np.linalg.norm(coordinates[i] - coordinates[j])
	return distmat


def initpara():
	'''

	:return:
	'''
	alpha = 0.99
	t = (1, 100)
	markovlen = 1000

	return alpha, t, markovlen


num = coordinates.shape[0]
distmat = getdistmat(coordinates)  # 得到距离矩阵

solutionnew = np.arange(num)
# valuenew = np.max(num)

solutioncurrent = solutionnew.copy()
valuecurrent = 99000  # 取一个较大值作为初始值
# print(valuecurrent)

solutionbest = solutionnew.copy()
valuebest = 99000  # np.max

alpha, t2, markovlen = initpara()
t = t2[1]

result = []  # 记录迭代过程中的最优解
while t > t2[0]:
	for i in np.arange(markovlen):

		# 下面的两交换和三角换是两种扰动方式，用于产生新解
		if np.random.rand() > 0.5:  # 交换路径中的这2个节点的顺序
			# np.random.rand()产生[0, 1)区间的均匀随机数
			while True:  # 产生两个不同的随机数
				loc1 = np.int(np.ceil(np.random.rand() * (num - 1)))
				loc2 = np.int(np.ceil(np.random.rand() * (num - 1)))
				## print(loc1,loc2)
				if loc1 != loc2:
					break
			solutionnew[loc1], solutionnew[loc2] = solutionnew[loc2], solutionnew[loc1]
		else:  # 三交换
			while True:
				loc1 = np.int(np.ceil(np.random.rand() * (num - 1)))
				loc2 = np.int(np.ceil(np.random.rand() * (num - 1)))
				loc3 = np.int(np.ceil(np.random.rand() * (num - 1)))

				if ((loc1 != loc2) & (loc2 != loc3) & (loc1 != loc3)):
					break

			# 下面的三个判断语句使得loc1<loc2<loc3
			if loc1 > loc2:
				loc1, loc2 = loc2, loc1
			if loc2 > loc3:
				loc2, loc3 = loc3, loc2
			if loc1 > loc2:
				loc1, loc2 = loc2, loc1

			# 下面的三行代码将[loc1,loc2)区间的数据插入到loc3之后
			tmplist = solutionnew[loc1:loc2].copy()
			solutionnew[loc1:loc3 - loc2 + 1 + loc1] = solutionnew[loc2:loc3 + 1].copy()
			solutionnew[loc3 - loc2 + 1 + loc1:loc3 + 1] = tmplist.copy()

		valuenew = 0
		for i in range(num - 1):
			valuenew += distmat[solutionnew[i]][solutionnew[i + 1]]
		valuenew += distmat[solutionnew[0]][solutionnew[29]]
		# print (valuenew)
		if valuenew < valuecurrent:  # 接受该解

			# 更新solutioncurrent 和solutionbest
			valuecurrent = valuenew
			solutioncurrent = solutionnew.copy()

			if valuenew < valuebest:
				valuebest = valuenew
				solutionbest = solutionnew.copy()
		else:  # 按一定的概率接受该解
			if np.random.rand() < np.exp(-(valuenew - valuecurrent) / t):
				valuecurrent = valuenew
				solutioncurrent = solutionnew.copy()
			else:
				solutionnew = solutioncurrent.copy()
	t = alpha * t
	result.append(valuebest)
	print(t)  # 程序运行时间较长，打印t来监视程序进展速度
# 用来显示结果

def draw(bestPath):
    '''

    :param bestPath:
    :return:
    '''
    ax = plt.subplot(111, aspect='equal')
    ax.plot(coordinates[:, 0], coordinates[:, 1], 'x', color='blue')
    for i, city in enumerate(coordinates):
        ax.text(city[0], city[1], str(i))
    ax.plot(coordinates[bestPath, 0], coordinates[bestPath, 1], color='red')
    plt.show()

print('最短路径为：', np.array(result[-1]))
for i in solutionbest:
	print(i, end="-->")
print(solutionbest[0])

plt.plot(np.array(result))
plt.ylabel("bestvalue")
plt.xlabel("t")
plt.show()
draw(solutionbest)


