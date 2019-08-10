N=int(input())
a=[i for i in input().split()[:N]]
b=0
for i in a:
    c=a.count(i)
    if b<c:
        b=c
print(b)
    
