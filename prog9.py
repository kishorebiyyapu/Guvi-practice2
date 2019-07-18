l,r=map(int,input().split())
a=[]
for i in range(l,r+1):
    c=0
    for j in range(2,i//2+1):
        if i%j==0:
            c=c+1
    if c==0:
        a.append(i)
print(len(a))
