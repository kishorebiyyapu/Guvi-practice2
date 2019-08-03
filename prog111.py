N,M=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in a[:N]]
c=[int(i) for i in a[N:N+M]]
d=[]
for i in b:
    if i in c:
        d.append(i)
d.sort()
for i in d:
    print(i,end=' ')
