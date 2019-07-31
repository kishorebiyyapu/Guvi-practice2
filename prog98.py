N,K=input().split()
N=[int(i) for i in N]
K=int(K)
for i in range(0,K+1):
    if i not in N:
        print("no")
        break
else:
    print("yes")
    
