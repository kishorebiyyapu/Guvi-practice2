N=int(input())
a=set(int(i) for i in input().split()[:N])
b=set(int(i) for i in input().split()[:N])
c=set(a.intersection(b))
for i in c:
    print(i,end=' ')
    
