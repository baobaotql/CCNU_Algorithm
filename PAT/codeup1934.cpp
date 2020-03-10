//codeup 1934
#include<stdio.h>

int main()
{
	int a[100];
	int n, x;
	while(scanf("%d", &n) != EOF)
	{
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
		}
		scanf("%d", &x); 	//find x
		int k;		//index 
		for(k = 0; k < n; k++)
		{
			if(a[k] == x)
			{
				printf("%d", k);
				break;	
			}
		}
		if(k == n)		//no finding
		{
			printf("no finding");
		}
	}
	return 0;
}
