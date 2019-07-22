N=int(input())
a=list(i for i in input().split()[:N])
for i in range(N):
    if a[i]=='0':
        print(a[i-1],end=" ")
    
