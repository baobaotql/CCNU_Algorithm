//pair
#include<iostream>
#include<string>
#include<map>
using namespace std;

int main()
{
	map<string, int> mp;
	mp.insert(make_pair("heihei", 5));
	mp.insert(pair<string, int>("haha", 10));
	for(map<string, int>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		cout << it->first << " " << it->second << endl;
	}
	return 0;
}
