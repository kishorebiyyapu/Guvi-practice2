N=int(input())
a=set(int(i) for i in input().split()[:N])
b=set(int(i) for i in input().split()[:N])
c=list(a.intersection(b))
c.sort()
for i in c:
    print(i,end=' ')
