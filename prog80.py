N=int(input())
a=[int(i) for i in input().split()[:N]]
a.sort()
print(a[1]-a[0])
