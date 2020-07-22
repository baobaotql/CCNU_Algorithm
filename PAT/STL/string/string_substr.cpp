//clear
#include<iostream>
#include<string>
using namespace std;

int main()
{
	string str = "Thank you for your smile";
	cout<< str.substr(0, 5) <<endl;
	cout<< str.substr(14, 4) << endl;
	cout<< str.substr(19, 5) <<endl;
	return 0;
}
