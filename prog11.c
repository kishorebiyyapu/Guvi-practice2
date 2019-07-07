#include<stdio.h>
#include<string.h>
int main()
{
	char a[100],b[100]="sunday",c[100]="saturday";
	gets(a);
	if(strcmp(a,b)==0)
	{
		printf("yes");
	}
	else if(strcmp(a,c)==0)
	{
		printf("yes");
	}
	else
	   printf("no");
	return 0;
}
