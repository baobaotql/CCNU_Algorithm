//find
#include<stdio.h>
#include<map>
using namespace std;

int main()
{
	map<char, int> mp;
	mp['a'] = 1;
	mp['b'] = 2;
	mp['c'] = 3;
	map<char, int>::iterator it = mp.find('b');
	printf("%c %d\n", it -> first, it -> second);
	return 0;
}
