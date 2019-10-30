#include<stdio.h>
#include<time.h>

int recursion(int n)
{
	if(n == 1 || n == 2)
	{
		return 1;
	}
	else
	{
		return recursion(n - 1) + recursion(n - 2);
	}
 } 
int non_recursion(int n)
{
	int sum = 0, sum_1 = 1, sum_2 = 1;
	if(n == 1 || n == 2)
	{
		return 1;
	}
	else
	{
		for(int i = 3; i >= n; i ++)
		{
			sum = sum_1 + sum_2;
			sum_2 = sum;
			sum_1 = sum_2;
		 } 
	}
	return sum;
 } 
 
 int main()
 {
 	int time_1, time_2, time_3, time_4;
 	int result_1, result_2;
 	int num_1, num_2;
 	
 	//递归 
 	printf("input a number : ");
 	scanf("%d", &num_1);
 	time_1 = clock();
 	result_1 = recursion(num_1);
 	time_2 = clock();
 	printf("%d\n", result_1);
	printf("running times : %dms\n", time_2 - time_1);
 	
 	//非递归 
 	printf("\ninput a number : ");
 	scanf("%d", &num_2);
 	time_3 = clock();
 	result_2 = recursion(num_2);
 	time_4 = clock();
 	printf("%d\n", result_2);
 	printf("running times : %dms", time_3 - time_2);
 	
 }
