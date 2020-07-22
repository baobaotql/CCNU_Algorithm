//operator
#include<iostream>
#include<string>
using namespace std;

int main()
{
	string str1 = "abc", str2 = "xyz", str3;
	str3 = str1 + str2;
	str1 += str2;
	cout<<str1<<endl;
	cout<<str3<<endl;
	return 0;
}
