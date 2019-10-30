#include<stdio.h>

int recursion(int n)
{
	int i;
	if(n==0)
	{
		return n;
	}
	else
	{
		recursion(n/2);
		printf("%d",n%2);	//因为输出在函数的后面 所以为逆序打印 
	}
 }  
 int non_resursion(int n)
 {
 	int s[100];
 	int i=0;
 	while(n>0)
 	{
 		s[i] = n%2;
 		i=i+1;
 		n=n/2;
	 }
	 for(i--;i>=0;i--)
	 {
	 	printf("%d", s[i]);
	 }
  } 
 
 int main()
 {
 	int num_1, num_2;
 	//递归 
 	printf("input a number : ");
 	scanf("%d", &num_1);
 	recursion(num_1);
 	printf("\r\n");
 	
 	//非递归 
 	printf("input a number : ");
 	scanf("%d", &num_2);
 	non_resursion(num_2);
 	
 	return 0;
 }
