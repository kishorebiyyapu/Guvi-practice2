N=int(input())
a=[int(i) for i in input().split()[:N]]
for i in range(N-1):
    if a[i]+2!=a[i+1]:
        print(a[i+1])
        break
