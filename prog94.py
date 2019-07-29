a=[i for i in input()]
for i in a:
    if a.count(i)>1:
        print("yes")
        break
else:
    print("no")
