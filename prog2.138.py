import math
N=int(input())
a=math.log(N,2)
if math.ceil(a)==math.floor(a):
    print("yes")
else:
    print("no")
