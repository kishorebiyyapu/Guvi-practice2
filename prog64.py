N,K=map(int,input().split())
a=list(int(i) for i in input().split()[:N])
b=[]
for i in a:
    if i<K:
        b.append(i)
b.sort()
for i in b:
    print(i,end=" ")
