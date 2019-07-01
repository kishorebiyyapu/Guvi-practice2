#include<stdio.h>
int main()
{
	int N,s=1,i;
	scanf("%d",&N);
	if(N==0)
	    printf("1");
	else
	{
	
	   for(i=1;i<=N;i++)
	   {
	   	s=s*i;
		     }
	   printf("%d",s);
	} 
	return 0;   
}
