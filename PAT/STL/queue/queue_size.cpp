//size
#include<stdio.h>
#include<queue>
using namespace std;

int main()
{
	queue<int> q;
	for(int i = 1; i <= 5; i++)
	{
		q.push(i);
	}
	printf("%d\n", q.size());
	return 0;
}
