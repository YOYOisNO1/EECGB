def program675():
    import math
    G = math.gcd
    F = math.floor
    import decimal
    D = decimal.Decimal
    l1 = [int(x) for x in input().split()]
    a,b,x,y  = l1[0],l1[1],l1[2],l1[3]
    f = G(x,y)
    x = D(x/f)
    y = D(y/f)
    width = a
    length = b
    #print(width,length)
    #print(x,y)
    if length<y or width<x:
        print(0)
    else:
        first = str((D(length/y)))
        if "." in first:
            first = "".join(list(first)[:first.index(".")])
        second = str(D(int(width/x)))
        if "." in second:
            second = "".join(list(second)[:second.index(".")])
        
        first1 = first.rjust(10**5,"0")
        second1 = second.rjust(10**5,"0")
        if first1>second1:
            print(second)
        else:
            print(first)
    