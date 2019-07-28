def fun(n):
    if n>1:
        fun(n//2)
    print(n%2,end=" ")    
a=int(input())
fun(a)
