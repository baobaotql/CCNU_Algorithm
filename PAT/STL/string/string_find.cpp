//find
#include<iostream>
#include<string>
using namespace std;

int main() 
{
	string str = "Thank you for your smile.";
	string str2 = "you";
	string str3 = "me";
	if(str.find(str2) != string::npos)
	{
		cout<<str.find(str2)<<endl;
	}
	if(str.find(str2, 7) != string::npos)
	{
		cout<<str.find(str2, 7)<<endl;
	}
	if(str.find(str3) != string::npos)
	{
		cout<<str.find(str3)<<endl;
	}
	else
	{
		cout<<"i know there is no position for me."<<endl;
	}
	return 0;
}
