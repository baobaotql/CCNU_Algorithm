//B1009
#include<stdio.h>
#include<string.h>

int main()
{
	char str[80];
	gets(str);
	int len=strlen(str);
	int r=0,h=0;
	char ans[80][80];
	
	for(int i;i<len;i++)
	{
		if(str[i]!=' ')
		{
			ans[r][h++]=str[i];
		}
		else
		{
			ans[r][h]='\0';
			r++;
			h=0;	
		}
	}
	for(int i=r;i>=0;i--)
	{
		printf("%s",ans[i]);
		if(i>0)
		{
			printf(" ");
		}
	}
	return 0;
}
