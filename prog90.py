N,K=map(int,input().split())
s=1
for i in range(1,K+1):
    s=(s*N)//i
    N=N-1
print(s)    
