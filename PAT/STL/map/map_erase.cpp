//erase
#include<stdio.h>
#include<map>
using namespace std;
/*
设置迭代器进行删除 
int main()
{
	map<char, int> mp;
	mp['a'] = 1;
	mp['b'] = 2;
	mp['c'] = 3;
	map<char, int>::iterator it = mp.find('b');
	mp.erase(it);
	for(map<char, int>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		printf("%c %d\n", it -> first, it -> second);
	} 
	return 0;
}
*/
/*
mp.erase(key) key作为预删除的映射的键 
int main()
{
	map<char, int> mp;
	mp['a'] = 1;
	mp['b'] = 2;
	mp['c'] = 3;
	mp.erase('b');
	for(map<char, int>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		printf("%c %d\n", it -> first, it -> second);
	}
	return 0;
}*/
int main()
{
	map<char, int> mp;
	mp['a'] = 1;
	mp['b'] = 2;
	mp['c'] = 3;
	map<char, int>::iterator it = mp.find('b');
	mp.erase(it, mp.end());
	for(map<char, int>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		printf("%c %d\n ", it -> first, it -> second);
	}
	return 0;
}
