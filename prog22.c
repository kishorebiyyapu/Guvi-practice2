#include<stdio.h>
int main()
{
	int N,K,i,a;
	scanf("%d%d",&N,&K);
	for(i=1;i<=N && i<=K;++i)
	{
		if(N%i==0 && K%i==0)
		{
		    a=i;
	    }
	}
	printf("%d",a);
	return 0;
}
