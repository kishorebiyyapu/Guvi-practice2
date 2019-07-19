import math
N,K=map(int,input().split())
a=math.log(N,K)
if math.ceil(a)==math.floor(a):
    print("yes")
else:
    print("no")
