N,l,r=map(int,input().split())
a=[int(i) for i in input().split()[:N]]
t=a[l-1]
for i in range(l-1,r):
    if t>a[i]:
        t=a[i]
print(t)
    
