#include<stdio.h>
#include<string.h>
int main()
{
	char a[100];
	int i,n,c,b[100],j,k;
	gets(a);
	n=strlen(a);
	strlwr(a);
	for(i=0;a[i]!='\0';i++)
	{
		c=0;
		for(j=0;a[j]!='\0';j++)
		{
			if(a[i]==a[j])
			{
				c=c+1;
			}
		}
		b[i]=c;
	}
	for(i=1;i<n;i++)
	{
		if(b[0]<b[i])
		{
			b[0]=b[i];
			k=i;
		}
	}
	printf("%c",a[k]);
	return 0;
}
