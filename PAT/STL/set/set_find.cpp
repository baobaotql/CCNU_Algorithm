//find()
#include<stdio.h>
#include<set>
using namespace std;

int main() 
{
	set<int> st;
	for(int i = 1; i <= 3; i++)
	{
		st.insert(i);
	}
	set<int>::iterator it = st.find(2);
	printf("have found %d ", *it);
	return 0;
}
