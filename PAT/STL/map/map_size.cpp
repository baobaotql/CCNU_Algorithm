//size
#include<stdio.h>
#include<map>
using namespace std;

int main()
{
	map<char, int> mp;
	mp['a'] = 10;
	mp['b'] = 20;
	mp['c'] = 30;
	prntf("%d\n", mp.size());
	return 0;
 } 
