#include<iostream>
#include<utility>
#include<string>

using namespace std;
int main()
{
	pair<string, int> p;
	p.first = "haha";
	p.second = 5;
	cout<<p.first <<" " <<p.second <<endl;
	p = make_pair("xixi", 55);
	cout<<p.first<< " "<<p.second <<endl;
	p = pair<string, int> ("heihei", 555);
	cout<<p.first <<" " <<p.second <<endl;
	return 0;
 } 
