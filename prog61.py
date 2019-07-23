N,K=map(int,input().split())
a=list(i for i in input().split()[:N])
d=0
for i in a:
    d=d+int(i)
if d==K:
    print("yes")
else:
    print("no")
