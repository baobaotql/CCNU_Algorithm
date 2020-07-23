//iterator
#include<stdio.h>
#include<map>
using namespace std;

int main()
{
	map<char, int> mp;
	mp['m'] = 20;
	mp['r'] = 30;
	mp['a'] = 40;
	for(map<char, int>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		printf("%c %d\n", it -> first, it -> second);
	}
	return 0;
}
