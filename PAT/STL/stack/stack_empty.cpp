//empty
#include<stdio.h>
#include<stack>
using namespace std;

int main()
{
	stack<int> st;
	if(st.empty() == true)
	{
		printf("Empty\n");
	}
	else
	{
		printf("Not Empty\n");
	}
	st.push(1);
	if(st.empty() == true)
	{
		printf("Empty\n");
	}
	else
	{
		printf("Not Empty\n");
	}
	return 0;
}
