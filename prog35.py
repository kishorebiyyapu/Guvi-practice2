a=input()
b=a.lower()
c=[i for i in b]
for i in c:
    if i==" ":
        c.remove(" ")
for i in c:
    if c.count(i)==1:
        print(i,end=" ")
