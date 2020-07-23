//repalce
#include<iostream>
#include<string>
using namespace std;

int main()
{
	string str = "Maybe you will turn around";
	string str2 = "will not";
	string str3 = "surely";
	cout<<str.replace(10, 4, str2) <<endl;
	cout<<str.replace(str.begin(), str.begin() + 4, str3) <<endl;
	return 0;
}
