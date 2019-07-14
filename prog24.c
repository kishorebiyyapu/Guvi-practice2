#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	char s[100];
	int i,c=0;
	gets(s);
	for(i=0;s[i]!='\0';i++)
	{
	
	if(isdigit(s[i])!=0)
	   c=c+1;
    }
    if(c==strlen(s))
       printf("yes");
    else
	   printf("no");   
	return 0;      
}
