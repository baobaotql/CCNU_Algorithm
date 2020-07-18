//get prinme
#include<stdio.h>
#include<math.h>

bool isPrime(int n)
{
	if(n <= 1) return false;
	int sqr = (int)sqrt(1.0 * n);
	for(int i = 2; i <= sqr; i++)
	{
		if(n % i == 0) return false;
	}
	return true;
}
int prime[101], pNum = 0;
bool p[101] = {0};
void Find_Prime()
{
	for(int i = 1; i < 101; i++)
	{
		if(isPrime(i) == true)
		{
			prime[pNum++] = i;
			p[i] = true;
		}
	}
}
int main()
{
	Find_Prime();
	for(int i = 0; i < pNum; i++)
	{
		printf("%d ", prime[i]);
	}
	return 0;
}
