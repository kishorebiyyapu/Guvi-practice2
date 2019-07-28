N,K=map(int,input().split())
s=1
for i in range(K):
    s=s*N
    N=N-1
print(s)    
