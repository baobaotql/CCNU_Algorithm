//pop
#include<stdio.h>
#include<queue>
using namespace std;

int main() 
{
	priority_queue<int> q;
	q.push(3);
	q.push(4);
	q.push(1);
	printf("%d\n", q.top());
	q.pop();
	printf("%d\n", q.top());
	return 0;
}
