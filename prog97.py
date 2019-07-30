l,r=map(int,input().split())
if l%2==0:
    l=l+1
s=0    
for i in range(l,r+1,2):
    s=s+i
print(s)
