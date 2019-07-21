A,B,C=map(int,input().split())
if A+B+C==180:
    if A!=0 and B!=0 and C!=0:
        print("yes")
    else:
        print("no")
else:
    print("no")
