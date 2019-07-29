N=int(input())
a=[int(i) for i in input().split()[:N]]
for i in range(1,N,2):
    t=a[i-1]
    a[i-1]=a[i]
    a[i]=t
for i in a:
    print(i,end=' ')
