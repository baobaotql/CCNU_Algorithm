//B1032

#include<stdio.h>
int schoolsum[100000]={0};
 	
 int main()
 {
 	int n,schoolid,schoolscore;
 	scanf("%d",&n);
 	for(int i=0;i<n;i++)
 	{
 		scanf("%d %d",&schoolid,&schoolscore);
 		schoolsum[schoolid]+=schoolscore;
	 }
	 int max=0;
	 int k;
	 for(int i=1;i<=n;i++)
	 {
	 	if(schoolsum[i]>max)
	 	{
	 		max=schoolsum[i];
	 		k=i;
		 }
	 }
	 printf("%d %d",k,max);
	 return 0;
 }
