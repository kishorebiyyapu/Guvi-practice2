#include<stdio.h>
int main()
{
	int N,K,a[100],b[100],i,j,c=1,t;
	scanf("%d%d",&N,&K);
	for(i=1;i<=N;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=1;i<=K;i++)
	{
		scanf("%d",&b[i]);
	}
	
	for(i=N+1;i<=N+K;i++)
	{
		a[i]=b[c];
		t=a[1];
	
		
	
		for(j=2;j<=i;j++)
		{
			if(a[j]>=t)
			{
				t=a[j];
				
			}
		}
		printf("%d ",t);
		c++;
	}
	return 0;
}
