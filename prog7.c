#include<stdio.h>
#include<string.h>
int main()
{
	int i;
	char a[100],t;
	gets(a);
	for(i=0;i<=strlen(a);i=i+2)
	{
		t=a[i];
		a[i]=a[i+1];
		a[i+1]=t;
	}
	puts(a);
	return 0;
}
