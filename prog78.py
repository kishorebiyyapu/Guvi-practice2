N,M=map(int,input().split())
a=[i for i in input().split()[:N]]
b=[i for i in input().split()[:M]]
a.extend(b)
a.sort()
for i in a:
    print(i,end=' ')
