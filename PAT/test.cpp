#include<stdio.h>

/*
//字符串是否出现 
const int maxn = 100;
char S[maxn][5], temp[5];
int hashTable[26*26*26 + 10];

int hashFunc(char S[], int len)
{
	int id = 0;
	for(int i = 0; i < len; i++)
	{
		id = id * 26 + (S[i] - 'A');
	}
	return id;
}

int main()
{
	int n, m;
	scanf("%d%d", &n, &m);
	
	for(int i = 0; i < m; i++)
	{
		scanf("%s", temp);
		int id = hashFunc(S[i], 3);
		hashTable[id]++;
	}
	for(int i = 0; i < m; i++)
	{
		scanf("%s", temp);
		int id = hashFunc(temp, 3);
		printf("%d\n", hashTable[id]);
	}
	return 0;
}
*/
/*
//数字是否出现 
const int maxn = 100010;
bool hashTable[maxn] = {false};

int main()
{
	int n, m, x;
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &x);
		hashTable[x] = true;
	}
	for(int i = 0; i < m; i++)
	{
		scanf("%d", &x);
		if(hashTable[x] == true)
		{
			printf("yes\n");
		}
		else
		{
			printf("No\n");
		}
	}
	return 0;
}
*/
/*
//数字出现统计 
const int maxn = 100010;
int hashTable[maxn] = {0};

int main() 
{
	int n, m, x;
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &x);
		hashTable[x]++;
	}
	for(int i = 0; i < m; i++)
	{
		scanf("%d", &x);
		printf("%d\n", hashTable[x]);
	}
	return 0;
}
*/

//递归 全排列
const int maxn = 11;
int n, P[maxn], hashTable[maxn] = {false};

void generateP(int index)
{
	if(index == n + 1)
	{
		for(int i = 1; i <= n; i++)
		{
			printf("%d", P[i]);
		}
		printf("\n");
		return;
	}
	for(int x = 1; x <= n; x++)
	{
		if(hashTable[x] == false)
		{
			P[index] = x;
			hashTable[x] = true;
			generateP(index + 1);
			hashTable[x] = false;
		}
	}
} 
int main()
{
	n = 3;
	generateP(1);
	return 0;
}


























































