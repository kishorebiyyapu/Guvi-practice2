#include<stdio.h>
#include<string.h>
int main()
{
	char S[100];
	int n,i;
	gets(S);
	n=strlen(S);
	S[0]=toupper(S[0]);
	for(i=0;i<n;i++)
	{
		if(S[i]==' ')
		{
			S[i+1]=toupper(S[i+1]);
		}
	}
	puts(S);
	return 0;
}
