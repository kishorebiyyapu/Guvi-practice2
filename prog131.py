N=[int(i) for i in input()]
s=0
for i in N:
    if i%2!=0:
        s=s+i
if s%2==0:
    print("E")
else:
    print("O")
