//insert
#include<iostream>
#include<string>
using namespace std;

int main()
{
	string str = "abcxyz", str2 = "opq";
	//insert(it, it2, it3)it2 it3是待插字符串的首位迭代器 
	str.insert(str.begin() + 3, str2.begin(), str2.end());
	cout<<str<<endl;
	return 0;
}
