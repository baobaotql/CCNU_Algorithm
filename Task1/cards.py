# -*- coding: utf-8 -*- 
# @Time : 2019/10/11 18:42 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : card.py 
# @Software: PyCharm

#non_recursion
s = [0]*52
print("initial state : ",s,"\n")

for i in range(1,52):
    for j in range(i,52):
        if((j+1)%(i+1)==0):
            if(s[j]==0):
                s[j]=1
            else:
                s[j]=0

print("ending state : ",s,"\n")

vec = [x+1 for x in range(52) if s[x]==0]
print("index : ",vec,"\n")



#recursion
s = [0]*52
print("initial state : ",s,"\n")

def turn_card(n):
    if(n>52):
        return
    else:
        for j in range(n,52):
            if ((j + 1) % (n + 1) == 0):
                if (s[j] == 0):
                    s[j] = 1
                else:
                    s[j] = 0
        turn_card(n+1)

turn_card(1)

print("ending state : ", s, "\n")

vec = [x+1 for x in range(52) if s[x]==0]
print("index : ",vec,"\n")
