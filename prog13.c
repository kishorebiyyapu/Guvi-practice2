#include<stdio.h>
int main()
{
	int N,b,r,c=0;
	scanf("%d",&N);
	b=N;
	while(b!=0)
	{
		r=b%10;
		c=c+(r*r);
		b=b/10;
	}
	printf("%d",c);
	return 0;
}
