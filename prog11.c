#include<stdio.h>
#include<string.h>
int main()
{
	char a[100],b[100]="Sunday",c[100]="Saturday";
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
