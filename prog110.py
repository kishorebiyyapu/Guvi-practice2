N=int(input())
a=[int(i) for i in input().split()[:N]]
s=0
if N==1:
    for i in a:
        print(i)
else:
    for i in a:
        s=s+i
    for i in a:
        print(s+i,end=' ')
