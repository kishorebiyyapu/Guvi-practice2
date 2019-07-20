S,N=input().split()
N=int(N)
a=[i for i in S]
while N>0:
    k=a[-1]
    a.pop()
    a.insert(0,k)
    N=N-1
for i in a:
    print(i,end="")
