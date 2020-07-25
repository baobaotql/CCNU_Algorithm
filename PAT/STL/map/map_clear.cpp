//clear
#include<stdio.h>
#include<map>
using namespace std;

int main() 
{
	map<char, int> mp;
	mp['a'] = 1;
	mp['b'] = 2;
	mp.clear();
	printf("%d \n", mp.size());
	return 0;
}
