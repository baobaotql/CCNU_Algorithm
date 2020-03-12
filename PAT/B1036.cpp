//B1036

#include<stdio.h>

int main() 
{
	int row, col;
	char c;
	scanf("%d %c", &col, &c);	//input col letter
	if(col % 2 == 1)
	{
		row = col / 2 + 1;
	}
	else
	{
		row = col / 2;
	}
	//1 row
	for(int i = 0; i < col; i++)
	{
		printf("%c", c);
	}
	printf("\n");
	//2~n-1 rows
	for(int i = 2; i < row; i++)
	{
		printf("%c", c);
		for(int j = 0; j < col - 2; j++)
		{
			printf(" ");
		}
		printf("%c\n", c);
	}
	// n row
	for(int i = 0; i < col ;i++)
	{
		printf("%c", c);
	 } 
	return 0;
}

