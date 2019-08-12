a=int(input())
b=[]
while a>1:
    c=a%2
    b.append(c)
    a=a//2
b.append(a)
n=len(b)
f=0
for i in range(n):
    f=f+1
    if b[i]==1:
        print(f)
        break;

