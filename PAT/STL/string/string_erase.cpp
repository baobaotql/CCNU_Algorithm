//erase
#include<iostream>
#include<string>
using namespace std;
/*single elements
int main() 
{
	string str = "abcdefg";
	str.erase(str.begin() + 4);
	cout<<str<<endl;
	return 0;
}
*/
int main()
{
	string str = "abcdefg";
	str.erase(str.begin() + 2, str.end() - 1);
	cout<<str<<endl;
	return 0;
}
