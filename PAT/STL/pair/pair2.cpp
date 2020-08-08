//pair
#include<iostream>
#include<utility>
#include<string>
using namespace std;

int main()
{
	pair<int, int> p1(5, 10);
	pair<int, int> p2(5, 15);
	pair<int, int> p3(10, 5);
	if(p1 < p3) printf("p1 < p3\n");
	if(p1 <= p3) printf("p1 <= p3\n");
	if(p1 < p2) printf("p1 < p2"); 
	return 0; 
 } 
