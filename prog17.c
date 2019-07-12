#include<stdio.h>
int main()
{
	int L,M,i=2;
	scanf("%d%d",&L,&M);
	while(i%L!=0 || i%M!=0){
		i++;
	}
	printf("%d",i);
	return 0;
}
