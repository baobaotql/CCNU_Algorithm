//PAT A1025

#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;
struct Student
{
	char id[15];	//准考证 
	int score;		//分数 
	int loc_num;	//考场号 
	int loc_rank;	//考场排名 
}stu[1000];

bool cmp(Student a, Student b)
{
	if(a.score != b.score) return a.score > b.score; 	//按照分数高到低排序 
	else return strcmp(a.id, b.id) < 0;		//分数相同 按准考证从小到大排 	
}
int main() 
{
	int n, k;
	int num = 0;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
	{
		scanf("%d", &k);	//考场内人数
		for(int j = 0; j < k; j++)
		{
			scanf("%s %d", stu[num].id, &stu[num].score);
			stu[num].loc_num = i;
			num++; 
		 } 
		 
		 sort(stu + num - k, stu + num, cmp);
		 
		 stu[num - k].loc_rank = 1;
		 
		 for(int j = num - k + 1; j < num; j++)
		 {
		 	if(stu[j].score == stu[j - 1].score)
		 	{
		 		stu[j].loc_rank = stu[j - 1].loc_rank;
			 }
			 else
			 {
			 	stu[j].loc_rank = j + 1 - (num - k);
			 }
		 }
	}
	printf("%d\n", num);
	
	sort(stu, stu + num, cmp);
	
	int r = 1;
	for(int i = 0; i < num; i++)
	{
		if(i > 0 && stu[i].score != stu[i - 1].score)
		{
			r = i + 1;
		}
		printf("%s ", stu[i].id);
		printf("%d %d %d\n", r, stu[i].loc_num, stu[i].loc_rank);
		
	}
	return 0;
}
