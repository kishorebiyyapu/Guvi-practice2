N=int(input())
a=[i for i in input()[:N]]
b=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in b:
        a.remove(i)
a=a[::-1]
for i in a:
    print(i,end='')
