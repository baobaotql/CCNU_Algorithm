//vector iterator
#include<stdio.h>
#include<vector>
using namespace std;

int main()
{
	vector<int> vi;
	for(int i = 1; i <= 5; i++)
	{
		vi.push_back(i);
	}
	vector<int>::iterator it = vi.begin();
	for(int i = 0; i < 5; i++)
	{
		printf("%d ", *(it + i));
	}
	return 0;
}
