import math
A=int(input())
c=math.radians(A)
b=math.sin(c)
if b>0 and b<1:
    print(round(b,1))
else:
    print(round(b))
