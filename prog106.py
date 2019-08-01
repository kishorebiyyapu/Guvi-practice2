N=int(input())
b=[]
a=[int(i) for i in input().split()[:N]]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=' ')
