//empty
#include<stdio.h>
#include<queue>
using namespace std;

int main()
{
	priority_queue<int> q;
	if(q.empty() == true)
	{
		printf("Empty\n");
	}
	else
	{
		printf("Not Empty\n");
	}
	q.push(1);
	if(q.empty() == true)
	{
		printf("Empty\n");
	}
	else
	{
		printf("Not Empty\n");
	}
	return 0;
}
