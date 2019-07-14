#include<stdio.h>
#include<ctype.h>
int main()
{ 
   char S[100];
   int i;
   gets(S);
   for(i=0;S[i]!='\0';i++)
   {
   	if(isupper(S[i])!=0)
   	     S[i]=S[i]+32;
   	else
	      S[i]=S[i]-32;     
   }
   puts(S);
   return 0;
}
