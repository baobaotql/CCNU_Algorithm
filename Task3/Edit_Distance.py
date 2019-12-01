# -*- coding: utf-8 -*- 
# @Time : 2019/12/1 17:25 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : Edit_Distance.py 
# @Software: PyCharm
'''
利用动态规划算法求解编辑距离问题
'''
def minDistance(word1, word2):
    '''

    :param word1: 传入字符串word1
    :param word2: 传入字符串Word2
    :return: 返回距离矩阵元素
    '''
    m = len(word1)
    n = len(word2)
    if m == 0:
        return n
    if n == 0:
        return m
    dp = [[0] * (n+1) for _ in range(m+1)] #初始化表格[m+1, n+1]
    # 计算边界
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1): #计算dp
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
    return dp[m][n]


if __name__ == "__main__":
    dis = minDistance('www.ccnu.edu.cn', 'www.neu.edu.cn')
    print("The longest Edit Distance is :", dis)

