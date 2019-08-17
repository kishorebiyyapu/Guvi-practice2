N=int(input())
a=[int(i) for i in input().split()[:N]]
for i in range(1,N):
    if (a[i]%a[i-1])==0:
        print(a[i],end=' ')
