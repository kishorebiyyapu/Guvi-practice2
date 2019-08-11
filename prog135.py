N=int(input())
if N%2==0:
    a=N//2
else:
    a=(N-1)//2
b=[int(i) for i in input().split()[:N]]
c=[int(i) for i in b[:a]]
d=[]
for i in range(a,N):
    d.append(b[i])
d.sort()
c.sort()
e=[]
e=d[::-1]
for i in c:
    print(i,end=' ')
for i in e:
    print(i,end=' ')

