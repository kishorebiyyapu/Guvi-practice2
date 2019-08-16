#include<stdio.h>
#include<stdlib.h>
struct node
{
	char d;
	struct node *next;
}*top=NULL,*temp=NULL;
void push(char b)
{
	temp=(struct node*)malloc(sizeof(struct node));
	temp->d=b;
	temp->next=NULL;
	if(top==NULL)
	{
		top=temp;
	}
	else
	{
		temp->next=top;
		top=temp;
		temp=NULL;
	}
}
char peek()
{
	if(top==NULL)
	{
	   return '0';	
	}
	else
	{
		return top->d;
	}
}
void pop()
{
	temp=top->next;
	top=temp;
	temp=NULL;
}
int length()
{
	int m;
	temp=top;
	while(temp!=NULL)
	{
		m=m+1;
	}
	return m;
}
int main()
{
	char a[100],c,d;
	int i,n;
	scanf("%s",&a);
	for(i=0;a[i]!='\0';i++)
	{
		if(a[i]=='{' || a[i]=='[' || a[i]=='(')
		{
			push(a[i]);
		}
		else if(a[i]=='}' || a[i]==']' || a[i]==')')
		{
			c=peek();
			if(a[i]=='}')
			    d='{';
			else if(a[i]==']')
			    d='[';
			else
			    d='(';
			if(c==d)
			{
				pop();
			}
			else
			{
				printf("no");
				goto re;
			}
		}
	}
	n=length();
	if(n==0)
	   printf("yes");
	else
	   printf("no");
	re:
	return 0;
}
