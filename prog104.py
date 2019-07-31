N=int(input())
a=[int(i) for i in input().split()[:N]]
s=0
for i in range(N-1):
    s=s+a[i]+a[i+1]
print(s)    
    
