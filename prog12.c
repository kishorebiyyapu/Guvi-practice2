#include<stdio.h>
int main()
{
	int a[100],N,K,i,b,c[100],t=0;
	scanf("%d%d",&N,&K);
	for(i=1;i<=N;i++)
	{
		scanf("%d",&a[i]);
	}
	b=K;
	while(b!=0)
	{
		for(i=1;i<=N;i++)
		{
		
			c[i+1]=a[i];

		}
		c[1]=a[N];
		for(i=1;i<=N;i++)
		{
			a[i]=c[i];
		}
		b=b-1;
	}
	for(i=1;i<=N;i++)
	{
		printf("%d ",c[i]);
	}
	return 0;
}
