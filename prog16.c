#include<stdio.h>
int main()
{
	int N,a[100],i,b[100],c,j;
	scanf("%d",&N);
	for(i=0;i<N;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<N;i++)
	{
		c=0;
		for(j=0;j<N;j++)
		{
			if(a[j]==a[i])
			{
				c=c+1;
			}
		}
		b[i]=c;
	}
	for(i=0;i<N;i++)
	{
		if(b[i]==1)
		    printf("%d",a[i]);
	}
	return 0;
}
