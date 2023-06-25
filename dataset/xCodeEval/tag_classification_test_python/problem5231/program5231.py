def program5231():
    a=int(input())
    b=[int (i) for i in input ().split ()]  
    c=0
    for i in range(len(b)):
        c+=abs(b[i])
    print(c)