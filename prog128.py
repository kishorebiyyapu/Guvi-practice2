N=int(input())
a=[int(i) for i in input().split()[:N]]
s=1
for i in a:
    s=s*i
if s%2==0:
    print("even")
else:
    print("odd")
