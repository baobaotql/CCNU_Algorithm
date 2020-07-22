//compare operator
#include<iostream>
#include<string>
using namespace std;

int main()
{
	string str1 = "aa", str2 = "aaa", str3 = "abc", str4 = "xyz";
	if(str1 < str2) printf("ok1\n");
	if(str1 != str3) printf("ok2\n");
	if(str4 >= str3) printf("ok3\n");
	return 0;
}
