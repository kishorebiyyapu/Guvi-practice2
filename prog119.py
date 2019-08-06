a=[i for i in input()]
a=a[::-1]
for i in range(len(a)):
    if a[i]=='A':
        a[i]='10'
    elif a[i]=='B':
        a[i]='11'
    elif a[i]=='C':
        a[i]='12'
    elif a[i]=='D':
        a[i]='13'
    elif a[i]=='E':
        a[i]='14'
    elif a[i]=='F':
        a[i]='15'
s=0
n=0
for i in a:
   s=(int(i)*pow(16,n))+s
   n=n+1
print(s)         
