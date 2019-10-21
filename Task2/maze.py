# -*- coding: utf-8 -*-
# @Time : 2019/10/19 10:26
# @Author : BaoBao
# @Mail : baobaotql@163.com
# @File : mzae.py
# @Software: PyCharm

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

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
    maze[x1][y1] = -1       #表示已经走过
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:   #到达终点
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0 : #找到了下一个
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = -1  # 标记为已经走过，防止死循环
                break
        else:   #八个方向都没找到
            maze[curNode[0]][curNode[1]] = -1  # 死路一条,标记下次不走
            stack.pop()     #回溯
    print("没有路")
    return False

mpath(1,1,8,8)