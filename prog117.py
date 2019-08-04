s=[i for i in input()]
s=s[::-1]
a=[]
for i in s:
    a.append(i)
    a.append('-')
a.pop()
for i in a:
    print(i,end='')
