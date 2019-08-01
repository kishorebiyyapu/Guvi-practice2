N=int(input())
a=[int(i) for i in input().split()[:N]]
d=dict()
for i in a:
    d[a.index(i)+1]=i
a.sort()    
for i in a:
    for key,value in d.items():
        if i==value:
            print(key,end=' ')

