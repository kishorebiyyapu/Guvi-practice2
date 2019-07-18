l,r=map(int,input().split())
for i in range(l+1,r):
    c=0
    for j in range(2,i//2+1):
        if i%j==0:
            c=c+1
    if c==0:
        print(i,end=" ")
