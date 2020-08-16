//next_permutation()
#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
	int a[10] = {1, 2, 3};
	do{
		printf("%d%d%d\n", a[0], a[1], a[2]);
	}while(next_permutation(a, a + 3));
	return 0;
}
