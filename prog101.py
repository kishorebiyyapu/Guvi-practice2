N=int(input())
s=0
a=[int(i) for i in input().split()[:N]]
for i in range(0,N-1):
    if a[i]<a[i+1]:
        s=s+a[i+1]
    else:
        s=s+a[i]
print(s)        
