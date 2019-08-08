N=int(input())
a=[]
for i in range(2,N):
    c=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            c=c+1
    if c==0:
        a.append(i)
for i in a:
    if N%i==0:
        print(i,end=' ')
