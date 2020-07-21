//eraser
//删除单个元素 st.eraser(it) it是所需要的删除元素的迭代器 
#include<stdio.h>
#include<set>
using namespace std;

int main()
{
	set<int> st;
	st.insert(100);
	st.insert(200);
	st.insert(100);
	st.insert(300);
	st.erase(st.find(100));
	st.erase(st.find(200));
	for(set<int>::iterator it = st.begin(); it != st.end(); it++)
	{
		printf("%d\n", *it);
	}
	return 0;
}
