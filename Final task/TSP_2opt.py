# -*- coding: utf-8 -*- 
# @Time : 2019/12/15 19:39 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : TSP_2opt.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

MAXCOUNT = 2000

# 城市的坐标
cities = np.array([
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
    [13, 40],
    [18, 40],
    [82, 7],
    [62, 32],
    [58, 35],
    [45, 21],
    [41, 26],
    [44, 35],
    [4, 50]
])

def calDist(xindex, yindex):
    '''

    :param xindex:
    :param yindex:
    :return:
    '''
    return (np.sum(np.power(cities[xindex] - cities[yindex], 2))) ** 0.5


def calPathDist(indexList):
    '''

    :param indexList:
    :return:
    '''
    sum = 0.0
    for i in range(1, len(indexList)):
        sum += calDist(indexList[i], indexList[i - 1])
    return sum

def pathCompare(path1, path2):
    '''

    :param path1:
    :param path2:
    :return:  path1长度比path2短则返回true
    '''
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False


def generateRandomPath(bestPath):
    '''

    :param bestPath:
    :return:
    '''
    a = np.random.randint(len(bestPath))
    while True:
        b = np.random.randint(len(bestPath))
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a + 1]
    else:
        return a, b, bestPath[a:b + 1]


def reversePath(path):
    '''

    :param path:
    :return: repath
    '''
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath


def updateBestPath(bestPath):
    '''

    :param bestPath:
    :return: bestpath
    '''
    count = 0
    while count < MAXCOUNT:
        print(calPathDist(bestPath))
        print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        if pathCompare(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end + 1] = rePath
    return bestPath


def draw(bestPath):
    '''

    :param bestPath:
    :return:
    '''
    ax = plt.subplot(111, aspect='equal')
    ax.plot(cities[:, 0], cities[:, 1], 'x', color='blue')
    for i, city in enumerate(cities):
        ax.text(city[0], city[1], str(i))
    ax.plot(cities[bestPath, 0], cities[bestPath, 1], color='red')
    plt.show()


def opt2():
    # 随便选择一条可行路径
    bestPath = np.arange(0, len(cities))
    bestPath = np.append(bestPath, 0)
    bestPath = updateBestPath(bestPath)
    draw(bestPath)

if __name__ =='__main__':
    opt2()
