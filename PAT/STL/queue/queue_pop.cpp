//pop
#include<queue>
#include<stdio.h>
using namespace std;

int main()
{
	queue<int> q;
	for(int i = 1; i <= 5; i++)
	{
		q.push(i);
	}
	for(int i = 1; i <= 3; i++)
	{
		q.pop();
	}
	printf("%d\n",q.front());
	return 0;
}
