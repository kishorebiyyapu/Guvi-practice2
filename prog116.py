N=int(input())
a=[i for i in input().split()]
b=set()
c=[]
d=[]
for i in a:
    if a.count(i)>1:
        b.add(i)
    else:
        c.append(i)
for i in b:
    d.append(i)
d.sort()
d=d[::-1]
c.sort()
c=c[::-1]
for i in d:
    print(i,end=' ')
for i in c:
    print(i,end=' ')
