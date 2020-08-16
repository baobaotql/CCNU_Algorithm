//lower_bound
//upper_bound
#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
	int a[10] = {1, 2, 2, 3, 3, 3, 5, 5, 5, 5};
	int* lowerPos = lower_bound(a, a + 10, -1);
	int* upperPos = upper_bound(a, a + 10, -1);
	printf("%d, %d\n", lowerPos - a, upperPos - a);
	
	lowerPos = lower_bound(a, a + 10, 1);
	upperPos = upper_bound(a, a + 10, 1);
	printf("%d, %d\n", lowerPos - a, upperPos - a);
	
	lowerPos = lower_bound(a, a + 10, 3);
	upperPos = upper_bound(a, a + 10, 3);
	printf("%d, %d\n", lowerPos - a, upperPos - a);
	
	lowerPos = lower_bound(a, a + 10, 4);
	upperPos = upper_bound(a, a + 10, 4);
	printf("%d, %d\n", lowerPos - a, upperPos - a);
	
	lowerPos = lower_bound(a, a + 10, 6);
	upperPos = upper_bound(a, a + 10, 6);
	printf("%d, %d\n", lowerPos - a, upperPos - a);
	
	return 0;
}
