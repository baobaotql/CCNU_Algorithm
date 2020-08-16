#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
	int a[10] = {10, 11, 12, 13, 14, 15};
	reverse(a, a + 4);
	for(int i = 0; i < 6; i++)
	{
		printf("%d ", a[i]);
	}
	return 0;
}
/*
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	string str = "abcdefghi";
	reverse(str.begin() + 2, str.begin() + 6);
	for(int i = 0; i < str.length(); i++)
	{
		printf("%c", str[i]);
	}
	return 0;
}
*/
