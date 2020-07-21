#include<stdio.h>
#include<vector>
using namespace std;
/*
//删除单个元素 
int main()
{
	vector<int> vi;
	for(int i = 5; i <= 9; i++)
	{
		vi.push_back(i);	//5 6 7 8 9
	}
	vi.erase(vi.begin() + 3);
	vector<int>::iterator it = vi.begin();
	for(int i = 0; i < vi.size(); i++)
	{
		printf("%d ", *(it + i));
	}
	return 0;
}
*/
//删除区间元素 
int main()
{
	vector<int> vi;
	for(int i = 5; i <= 9; i++)
	{
		vi.push_back(i);	// 5 6 7 8 9
	}
	vi.erase(vi.begin() + 1, vi.begin() + 4);
	for(int i = 0; i < vi.size(); i++)
	{
		printf("%d ", vi[i]);	//5  9
	 } 
	 return 0;
}

















