N,K=map(int,input().split())
a=list(i for i in input().split()[:N])
s=0
for i in a:
    s=s+int(i)
if s==K:
    print("yes")
else:
    print("no")
