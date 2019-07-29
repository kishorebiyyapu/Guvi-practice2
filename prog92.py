a=[int(i) for i in input()]
j=0
s=0
for i in range(len(a)-1,-1,-1):
    s=s+(pow(2,j)*a[i])
    j=j+1
print(s)
