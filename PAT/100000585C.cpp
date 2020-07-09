//100000585C
#include<iostream>
#include<algorithm>
using namespace std;

int BinarySearch(int A[], int left, int right, int x)
{
	int mid;	//Ä¬ÈÏÉıĞò 
	while(left <= right)
	{
		mid = (left + right) / 2;
		if(A[mid] == x)
		{
			return mid;
		}
		else if(A[mid] > x)
		{
			right = mid - 1;
		}
		else
		{
			left = mid + 1;
		}
	}
	return -1;
}

int main() 
{
	int n, m;
	while(scanf("%d", &n))
	{
		int a[n];
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
		}
		scanf("%d", &m);
		sort(a, a + n);
		while(m--)
		{
			int x;
			scanf("%d", &x);
			int e;
			e = BinarySearch(a, 0, n - 1, x);
			if(e != -1) printf("Yes\n");
			else printf("No\n");
		}
	}
	return 0;
}
