//100000586B
#include<stdio.h>
#include<algorithm>

using namespace std;


int Partition(int A[], int left, int right)
{
	int temp = A[left];
	while(left < right)
	{
		while(left < right && A[right] > temp)
			right --;
		A[left] = A[right];
		
		while(left < right && A[left] <= temp)
			left ++;
		A[right] = A[left];
	}
	A[left] = temp;
	return left;
}

void QuickSort(int A[], int left, int right)
{
	if(left < right)
	{
		int pos = Partition(A, left, right);
		QuickSort(A, left, pos - 1);
		QuickSort(A, pos + 1, right);
	}
}

int main()
{
	int m;
	while(scanf("%d", &m) != EOF)
	{
		int a[m];
		for(int i = 0; i < m; i++)
		{
			scanf("%d", &a[i]);
		}
		QuickSort(a, 0, m - 1);
		for(int i = 0; i < m; i++)
		{
			printf("%d\n", a[i]);
		}
	 } 
}
