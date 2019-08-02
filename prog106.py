N=int(input())
c=[]
a=[int(i) for i in input().split()[:N]]
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    print(i,end=' ')
