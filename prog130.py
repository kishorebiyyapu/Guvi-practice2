N=int(input())
a=[int(i) for i in input().split()[:N]]
s=0
b=[]
for i in a:
    if i==1:
        s=s+i
        b.append(s)
    elif i%2==0:
        s=s+i
        b.append(s)
    else:
        b.append(i)
for i in b:
    print(i,end=' ')
    
