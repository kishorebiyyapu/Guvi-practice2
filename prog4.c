#include<stdio.h>
#include<string.h>
int main()
{
	char s[100];
	int i,n;
	gets(s);
	n=strlen(s);
	n=n+1;
	for(i=0;i<n;i++)
	{
		if(s[i]=='\0')
		{
			s[i]='.';
			s[i+1]='\0';
		}
	}
    puts(s);
	return 0;
}
