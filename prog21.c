#include<stdio.h>
int main()
{
	int a,b,c,d,e,f;
	scanf("%d%d",&a,&b);
	scanf("%d%d",&c,&d);
	scanf("%d%d",&e,&f);
	if(a==c && c==e)
	     printf("yes");
	else if(b==d && b==f)
	     printf("yes");
	else
	      printf("no");
	return 0;	  	      
}
