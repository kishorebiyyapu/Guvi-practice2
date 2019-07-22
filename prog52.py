N,K=map(int,input().split())
a=list(i for i in input().split()[:N])
a.sort()
print(a[K-1])
