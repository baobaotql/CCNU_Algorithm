//insert()
#include<stdio.h>
#include<vector>
using namespace std;

int main()
{
	vector<int> vi;
	for(int i = 1; i <= 5; i++)
	{
		vi.push_back(i);	//1 2 3 4 5
	}
	vi.insert(vi.begin() + 2, -1);
	
	for(int i = 0; i < vi.size(); i++)
	{
		printf("%d ", vi[i]);	//1 2 -1 3 4 5
	}
	return 0;
}
