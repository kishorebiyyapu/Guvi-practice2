N=int(input())
for i in range(1,N+1):
    if N%i==0 and (N//i)%2!=0:
        print(i)
        break
