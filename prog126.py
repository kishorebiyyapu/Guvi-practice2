N,K=map(int,input().split())
a=[i for i in input().split()[:N]]
b=a.copy()
for i in a:
    if a.count(i)>=1:
        a.remove(i)
c=[]
for i in b:
    if b.count(i)< K:
        c.append(i)
c.sort()
for i in c:
    print(i,end=' ')
