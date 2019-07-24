N=int(input())
a=[int(i) for i in input().split()[:N]]
for i in a:
    if N>i:
        print(i,end=' ')
