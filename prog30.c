#include<stdio.h>
int main()
{
	char a[100],b[100];
	int K,i,c=0,d=0;
	scanf("%s%s%d",&a,&b,&K);
    for(i=0;a[i]!='\0';i++)
    {
    	c=c+1;
	}
	for(i=0;i<c;i++)
	{
		if(a[i]!=b[i])
		   d=d+1;
	}
	if(d==K)
	   printf("yes");
	else
	   printf("no");   
	return 0;
}
