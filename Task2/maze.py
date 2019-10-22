 -*- coding: utf-8 -*-
# @Time : 2019/10/19 10:26
# @Author : BaoBao
# @Mail : baobaotql@163.com
# @File : mzae.py
# @Software: PyCharm
import numpy as np

maze =np.array ([
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0],
])

p = np.array([1, 1, 1, 1, 1, 1, 1, 1])
q = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

a = np.insert(maze, 0, values=p, axis=1)
b = np.insert(a, 9,values=p, axis=1)

c = np.insert(b, 0, values=q, axis=0)
d = np.insert(c, 9, values=q, axis=0)

print("初始化迷宫：")
print(d)#为解决越界问题 初始化迷宫

dirs = [lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x, y + 1),
        lambda x, y: (x + 1, y - 1),
        lambda x, y: (x + 1, y + 1),
        lambda x, y: (x - 1, y - 1),
        lambda x, y: (x - 1, y + 1)
        ]

def mpath(x1, y1, x2, y2):
    stack = []      #建立抽象栈
    stack.append((x1, y1))      #加入初始点
    d[x1][y1] = -1       #表示已经走过
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode == (x2, y2):
            print(stack)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if d[nextNode[0]][nextNode[1]] == 0 : #找到了下一个
                stack.append(nextNode)
                d[nextNode[0]][nextNode[1]] = -1  # 标记为已经走过，防止死循环
                break

        else:   #八个方向都没找到
            d[curNode[0]][curNode[1]] = -1  # 死路一条,标记下次不走
            stack.pop()  #回溯

    print("没有路")
    return False

mpath(1,1,8,8)
