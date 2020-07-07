//100000585A
#include<stdio.h>

int main()
{
	int n;
	int array[200];
	while(scanf("%d", &n) != EOF)
	{
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &array[i]);
		}
		
		int x;
		scanf("%d", &x);
		
		int flag = 1;
		for(int i = 0; i < n; i++)
		{
			if(array[i] == x)
			{
				printf("%d\n", i);
				flag = 0;
			}
		}
	 	if(flag == 1)
	 	{
	 		printf("-1\n");
		 }
	}
	
	return 0;
}
