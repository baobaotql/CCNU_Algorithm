#include <cstdio>

const int maxn = 30;

int n, V, maxValue = 0;	//物品件数 背包容量 最大价值
int w[maxn], c[maxn];	//每件物品的重量 每件物品的价值

void DFS(int index, int sumW, int sumC)
{
	if(index == n)
	{
		if(sumW <= V && sumC >= maxValue)
		{
			maxValue = sumC;
		}
		return;
	}
	DFS(index + 1, sumW, sumC);
	DFS(index + 1, sumW + w[index], sumC + c[index]);
}
int main()
{
	scanf("%d%d", &n, &V);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &w[i]);
	}
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &c[i]);
	}
	DFS(0, 0, 0);
	printf("%d\n", maxValue);
	return 0;
}
