N,K=map(int,input().split())
a=list(int(i) for i in input().split()[:N])
for i in a:
    if i<K:
        print(i,end=" ")
