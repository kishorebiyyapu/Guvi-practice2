N=int(input())
a=[int(i) for i in input().split()[:N]]
b=max(a)
for i in range(5,0,-1):
    c=0
    for j in a:
        if j%i==0:
            c=c+1
    if c==N:
        print(i)
        break
