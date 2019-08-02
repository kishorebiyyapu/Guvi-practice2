N=int(input())
a=[int(i) for i in input().split()[:N]]
for i in range(N):
    s=0
    for j in range(i+1):
        s=s+a[j]
    print(s,end=' ')        
        
