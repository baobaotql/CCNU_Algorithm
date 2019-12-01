# -*- coding: utf-8 -*- 
# @Time : 2019/12/1 17:32 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : LCS.py 
# @Software: PyCharm

import numpy as np

def Longest_Common_Subsequence(a, b):
    '''

    :param a:字符串a
    :param b:字符串b
    :return:length
            subseq
    '''
    length = 0
    subseq = ''
    cell = np.zeros(shape=(len(a), len(b)))
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                cell[i][j] = cell[i - 1][j - 1] + 1
                if cell[i][j] > length:
                    length = cell[i][j]
                    subseq += a[i]
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return length, subseq

if __name__ == "__main__":
    a, b = Longest_Common_Subsequence('www.ccnu.edu.cn', 'www.neu.edu.cn')
    print('The length of longest common subsequence is：%d\nThe Longest Common Subsequence is：%s' % (a, b))
