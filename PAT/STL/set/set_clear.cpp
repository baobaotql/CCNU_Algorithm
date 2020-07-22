//clear
#include<stdio.h>
#include<set>
using namespace std;

int main()
{
	set<int> st;
	st.insert(2);
	st.insert(5);
	st.insert(4);
	st.clear();
	printf("%d", st.size());
	return 0;
}
