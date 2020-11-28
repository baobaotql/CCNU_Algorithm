 #include<cstdio>
 #include<cstring>

const int maxn = 10010;
struct Node
{
	char data;
	int next;
	bool flag;	//单端节点是否在第一条链表中出现过
}node[maxn];

int main()
{
	for(int i = 0; i < maxn; i++)
	{
		node[i].flag = false;
	}
	int s1, s2, n;
	scanf("%d%d%d", &s1, &s2, &n);
	int address, next;	//结点地址 后继结点地址
	char data;
	for(int i = 0; i < n; i++)
	{
		scanf("%d %c %d", &address, &data, &next);
		node[address].data = data;
		node[address].next = next;
	}
	int p;
	for(p = s1; p != -1; p = node[p].next)
	{
		node[p].flag = true;
	}
	for(p = s2; p != -1; p = node[p].next)
	{
		if(node[p].flag == true)
			break;
	}
	if(p != -1)
	{
		printf("%05d\n", p);
	}
	else
	{
		printf("-1\n");
	}
	return 0;
}
