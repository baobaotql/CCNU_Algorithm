#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
bool cmp(int a,int b)
{
    return a>b;
}
int main()
{
    int N;
    cin>>N;
    int m=0,n=0,min=N;
    for(int i=0;i<=N;i++){
        for(int j=0;j<=i;j++){
            if(i*j==N&&(i-j)<min){
                //寻找差最小的数，并记录下来
                min=i-j;
                m=i;
                n=j;
            }
        }
    }
    int matrix[m][n];
    memset(matrix,0,sizeof(matrix));
    int num[N];
    for(int i=0;i<N;i++) cin>>num[i];
    sort(num,num+N,cmp);
    int i=0,j=0,k=0;
    matrix[i][j]=num[k++];
    while(k<N)
    {
        while(j+1<n&&!matrix[i][j+1])    matrix[i][++j]=num[k++];//先往右
        while(i+1<m&&!matrix[i+1][j])    matrix[++i][j]=num[k++];//再往下
        while(i-1>=0&&!matrix[i-1][j])   matrix[--i][j]=num[k++];//再往左
        while(j-1>=0&&!matrix[i][j-1])   matrix[i][--j]=num[k++];//再往上
    }
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<matrix[i][j];
            if(j<n-1)cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
