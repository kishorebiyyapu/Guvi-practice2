N,K=map(int,input().split())
a=[int(i) for i in input().split()[:N]]
b=a.count(K)
if b>0:
    print("yes",end=' ')
    print(b)
else:
    print("no")
    
