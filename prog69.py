N,K=map(int,input().split())
a=[int(i) for i in input().split()[:N]]
for i in range(N-K):
    print(a[i],end=' ')
