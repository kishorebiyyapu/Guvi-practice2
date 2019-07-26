N=int(input())
a=[i for i in input().split()[:N]]
for i in range(N-1):
    if a[i]>a[i+1]:
        print(a[i])
