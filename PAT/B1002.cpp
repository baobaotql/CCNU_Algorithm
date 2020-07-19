#include <stdio.h>
#include <string.h>
int main()
{
    char c[100];
    int a[5];
    char pinyin[][9] = { "ling","yi","er","san","si","wu","liu","qi","ba","jiu"};
    int i,n,t;
    n = 0;
    t = 0;
    gets(c);
    for(i=0;i<strlen(c);i++)
        n = n + c[i] - 48;
    while (n!=0)
    {
        a[t] = n%10;
        n = n/10;
        t++;
    }
    printf("%s",pinyin[a[t-1]]);
    for(i=t-2;i>=0;i--)
        printf(" %s",pinyin[a[i]]);
} 
