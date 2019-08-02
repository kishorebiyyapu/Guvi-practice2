N=int(input())
b=[int(i) for i in input().split()[:N]]
d=dict()
for i in b:
    d[b.index(i)+1]=i
b.sort()    
for i in b:
    for key,value in d.items():
        if i==value:
            print(key,end=' ')

