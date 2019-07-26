N=int(input())
a=[int(i) for i in input().split()[:N]]
b=[]
for i in range(N-1):
    if a[i]>a[i+1]:
        b.append(i+1)
b.append(N)            
h=b[0]
for i in range(len(b)-1):
    if h<b[i+1]-b[i]:
        h=b[i+1]-b[i]
print(h)        
    
