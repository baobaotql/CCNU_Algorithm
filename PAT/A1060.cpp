//A1060
/*算法思路：
首先判断首字符是不是以零开头，是0就先去掉0，然后看现在的首字符是不是小数点
是小数点的话就去掉小数点，并且去掉小数点后非0位前的所有0
若去掉前导0后 不是小数点 那么找到后面的小数点并去掉*/
#include<iostream>
#include<string>
using namespace std;

int n;
string deal(string s, int e)
{
	int k = 0;
	while(s.length() > 0 && s[0] == '0')
	{
		s.erase(s.begin());
	}
	if(s[0] == '.')
	{
		s.erase(s.begin());
		while(s.length() > 0 && s[0] == '0')
		{
			s.erase(s.begin());
			e --;
		}
	}
	else
	{
		while(k < s.length() && s[k] != '.')
		{
			k ++;
			e ++;
		}
		if(k < s.length())
		{
			s.erase(s.begin() + k);
		}
	}
	if(s.length() == 0)
	{
		e = 0;
	}
	int num = 0;
	k = 0;
	string res;
	while(num < n)
	{
		if(k < s.length()) res += s[k++];
		else res += '0';
		num ++;
	}
	return res;
 } 
int main()
{
	string s1, s2, s3, s4;
	cin>> n>> s1>> s2;
	int e1 = 0, e2 = 0;
	s3 = deal(s1, e1);
	s4 = deal(s2, e2);
	if(s3 == s4 && e1 == e2)
	{
		cout<< "Yes 0."<< s3<< "*10^"<< e1<< endl;
	 } 
	 else
	 {
	 	cout<< "No 0."<< s3<< "*10^"<< e1<< " 0."<< s4<< "*10^"<< e2<< endl;
	 }
	 return 0;
} 
 
 

