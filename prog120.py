a=int(input())
n=0
s=1
while s<=a:
    s=pow(2,n)
    n=n+1
if a==0 or a==1:
    print(1)
else:
    print(n-1)    
