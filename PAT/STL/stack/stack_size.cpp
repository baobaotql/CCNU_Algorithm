//size
#include<stdio.h>
#include<stack>
using namespace std;

int main()
{
	stack<int> st;
	for(int i = 1; i<= 5; i++)
	{
		st.push(i);
	}
	printf("%d\n", st.size());
	return 0;
}
