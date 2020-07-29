//B1060
#include<iostream>
#include<string>
#include<vector>
using namespace std;
 
int main()
{
	string s1, s2, s3, s4;
	cin >> s1 >> s2 >> s3 >> s4;
	int i = 0; string ss[7] = { "MON","TUE","WED","THU","FRI","SAT","SUN" };
	while (s1[i] != '\0'&&s2[i] != '\0')
	{
		if (s1[i] == s2[i] && s1[i] >= 'A'&&s1[i] <= 'G')
		{
			cout << ss[s1[i] - 'A'] << " "; break;
		}
		i++;
	}
	i++;
	while (s1[i] != '\0'&&s2[i] != '\0')
	{
		if (s1[i] == s2[i] )
		{
			if (s1[i] >= 'A'&&s1[i] <= 'N')
			{
				cout << int(s1[i] - 'A' + 10) << ":";
				break;
			}
			if (s1[i] >= '0'&&s1[i] <= '9')
			{
				cout << "0" << s1[i] << ":";
				break;
			}
		}
		i++;
	}
	int j = 0; 
	while (s3[j] != '\0'&&s4[j] != '\0')
	{
		if (s3[j] == s4[j] && (s3[j] >= 'a'&&s3[j] <= 'z' || s3[j] >= 'A'&&s3[j] <= 'Z'))
		{
			if (j < 10)
				cout << "0" << j;
			else
				cout << j;
			break;
		}
		j++;
	}
} 
