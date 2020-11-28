
#include <iostream>
#include<cstdio>
#include <stdio.h>
#include <stack>
#include <queue>
#include <map>

using  namespace std;

struct node{
    double num;
    char op;
    bool flag;	//true表示操作数，false表示操作符
};

string str;
stack< node > s;
queue< node > q;

map< char , int> op;

void change(string str)
{
    for (int i = 0; i <str.length() ;) {
        if(str[i]>='0' && str[i] <='9')	//如果是数字
        {
            struct node temp;
            temp.flag = true;
            temp.num = str[i] - '0';
            i++;
            while (i <str.length()&&str[i]>='0' && str[i] <='9' )
            {
                temp.num = temp.num * 10 + (str[i] - '0');
                i++;
            }
            q.push(temp);
        }
        else if(str[i]=='(' || str[i]==')')
        {
            if(str[i] == '(')
            {
                struct node x;
                x.op = str[i];
                x.flag = false;
                s.push(x);
            }else
            {
                while (s.top().op!='(')
                {
                    q.push(s.top());
                    s.pop();
                }
                s.pop();	//在栈中去除左括号
            }
            i++;
        }else
        {
            struct node temp;
            temp.flag = false;
            temp.op = str[i];
            while(!s.empty()&&op[temp.op] <=op[s.top().op])
            {
                q.push(s.top());
                s.pop();
            }
            s.push(temp);
            i++;
        }
    }

    //在遍历完中缀表达式后，把栈中的操作符一次弹出到后缀表达式中
    while(!s.empty())
    {
        q.push(s.top());
        s.pop();
    }
}
double cal()
{
    node cur;
    node temp;
    double temp1,temp2;
    while(!q.empty())
    {
        cur = q.front();
        q.pop();
        if(cur.flag == true)
        {
            s.push(cur);
        }else
        {
            temp2 = s.top().num ;
            s.pop();
            temp1 = s.top().num;
            s.pop();
            temp.flag = true;
            if(cur.op =='+')
            {
                temp.num = temp1 + temp2;
            }else if(cur.op =='-')
            {
                temp.num = temp1 - temp2;
            }else if(cur.op =='*')
            {
                temp.num = temp1 * temp2;
            }else if(cur.op =='/')
            {
                temp.num = temp1 / temp2;
            }
            s.push(temp);
        }
    }
    return s.top().num;
}
int main(void)
{
//    这里设置为1和2其实是有门道的，因为‘（’默认为0了，优先级最低
    op['+'] = op['-'] = 1;
    op['*'] = op['/'] = 2;
    while(getline(cin,str),str!="0")	//由于cin读取字符串时，遇到空格就会停止，所以用了getline，可以读一行
    {
        for(string::iterator it =str.end(); it!=str.begin();it--)
        {
            if(*it == ' ')
            {
                str.erase(it);//把表达式中的空格全部去掉
            }
        }
        while(!s.empty())
        {
            s.pop();//初始化
        }
        change(str);//转为后缀表达式
        printf("%.2f",cal());
    }
}

