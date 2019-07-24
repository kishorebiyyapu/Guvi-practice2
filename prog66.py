N,K=map(int,input().split())
a=[i for i in input().split()[:N]]
for i in a:
    if a.count(i)==K:
        print(i)
        break
    
