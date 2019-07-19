N=int(input())
a=list(map(int,input().split()[:N]))
b=sorted(a)
if a==b:
    print("yes")
else:
    print("no")
