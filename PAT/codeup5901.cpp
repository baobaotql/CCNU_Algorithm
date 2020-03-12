//codeup 5901
#include<stdio.h>
#include<string.h>

bool judge(char str[])
{
	int len = strlen(str);
	for(int i = 0; i < len / 2; i++)
	{
		if(str[i] != str[len - i - 1])
			return false;
	}
	return true;
}

int main()
{
	char str[255];
	while(gets(str))
	{
		bool flag = judge(str);
		if(flag == true)
		{
			printf("YES\n");
		}
		else
		{
			printf("No\n");
		}
	}
	return 0;
}
