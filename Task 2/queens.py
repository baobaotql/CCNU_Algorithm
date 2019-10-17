# -*- coding: utf-8 -*- 
# @Time : 2019/10/12 17:00 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : queens.py 
# @Software: PyCharm
def is_rule(queen_tup, new_queen):
    """
    :param queen_tup: 棋子队列，用于保存已经放置好的棋子，数值代表相应棋子列号
    :param new_queen: 被检测棋子，数值代表列号
    :return: True表示符合规则，False表示不符合规则
    """
    num = len(queen_tup)
    for index, queen in enumerate(queen_tup):

        if new_queen == queen:  # 判断列号是否相等
            return False
        if abs(new_queen - queen) == num - index:  # 判断列号之差绝对值是否与行号之差相等
            return False

    return True

# -*- coding: utf-8 -*- 
# @Time : 2019/10/12 17:00 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : queens.py 
# @Software: PyCharm
def is_rule(queen_tup, new_queen):
    """
    :param queen_tup: 棋子队列，用于保存已经放置好的棋子，数值代表相应棋子列号
    :param new_queen: 被检测棋子，数值代表列号
    :return: True表示符合规则，False表示不符合规则
    """
    num = len(queen_tup)
    for index, queen in enumerate(queen_tup):

        if new_queen == queen:  # 判断列号是否相等
            return False
        if abs(new_queen - queen) == num - index:  # 判断列号之差绝对值是否与行号之差相等
            return False

    return True


def arrange_queen(num, queen_tup=list()):
    """
    :param num:棋盘的的行数，当然数值也等于棋盘的列数
    :param queen_tup: 设置一个空队列，用于保存符合规则的棋子的信息
    """

    for new_queen in range(num):  # 遍历一行棋子的每一列

        if is_rule(queen_tup, new_queen):  # 判断是否冲突

            if len(queen_tup) == num - 1:  # 判断是否是最后一行
                yield [new_queen]  # yield关键字

            else:
                # 若果不是最后一行，递归函数接着放置棋子
                for result in arrange_queen(num, queen_tup + [new_queen]):
                    yield [new_queen] + result


for i in arrange_queen(8):
    print(i)

    #


def arrange_queen(num, queen_tup=list()):
    """
    :param num:棋盘的的行数，当然数值也等于棋盘的列数
    :param queen_tup: 设置一个空队列，用于保存符合规则的棋子的信息
    """

    for new_queen in range(num):  # 遍历一行棋子的每一列

        if is_rule(queen_tup, new_queen):  # 判断是否冲突

            if len(queen_tup) == num - 1:  # 判断是否是最后一行
                yield [new_queen]  # yield关键字

            else:
                # 若果不是最后一行，递归函数接着放置棋子
                for result in arrange_queen(num, queen_tup + [new_queen]):
                    yield [new_queen] + result


for i in arrange_queen(8):
    print(i)
