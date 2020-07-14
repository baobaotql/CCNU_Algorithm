//100000586C
#include<stdio.h>
int a[1000];

int partition(int A[], int left, int right)
{
	int temp = a[left];
	while(left < right)
	{
		while(left < right && a[right] > temp)
			right --;
		a[left] = a[right];
		while(left <right && a[left] < temp)
			left ++;
		a[right] = a[left];
	}
	a[left] = temp;
	return left;
}

void QuickSort(int a[], int left, int right)
{
	if(left <right)
	{
		int pos = partition(a, left, right);
		QuickSort(a, left, pos - 1);
		QuickSort(a, pos + 1, right);
	}
}

int main()
{
	int n;
	while(scanf("%d", &n))
	{
		for(int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		QuickSort(a, 0, n - 1);
		for(int i = 0; i < n; i++)
			printf("%d\n", a[i]);
	}
	return 0;
}
