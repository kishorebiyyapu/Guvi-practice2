a=int(input())
if a>=-2**15+1 and a<=2**15+1:
    print("INT")
elif a>=-2**31+1 and a<=2**31+1:
    print("LONG")
else:
    print("LONG LONG")
