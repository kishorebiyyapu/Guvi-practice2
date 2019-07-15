#include<stdio.h>
#include<math.h>
int main()
{
	int l,r,c=0,i;
	scanf("%d%d",&l,&r);
	for(i=l;i<=r;i++)
	{
		if(sqrt(i)==floor(sqrt(i)))
		    c=c+1;
	}
	printf("%d",c);
	
	return 0;
}
