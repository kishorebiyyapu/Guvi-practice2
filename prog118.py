a=[i for i in input().split()]
for i in range(1,len(a)):
    if len(a[0])<len(a[i]):
        a[0]=a[i]
print(a[0])
