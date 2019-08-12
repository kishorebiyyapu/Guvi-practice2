a=int(input())
b=[]
while a>1:
    c=a%2
    b.append(c)
    a=a//2
b.append(a)
c=b.count(1)
print(c)
