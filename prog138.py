import math
m=int(input())
z=math.log(m,2)
if math.ceil(z)==math.floor(z):
    print("yes")
else:
    print("no")
