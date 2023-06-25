def program4319():
    import math
    
    
    n = int(input())
    
    s = sum(map(int, str(n)))
    d = math.sqrt(s ** 2 + 4 * n))
    
    x1 = (-s + d) / 2 
    x2 = (-s - d) / 2 
    
    intx1 = int(x1)
    intx2 = int(x2)
    
    if intx2 == x2:
        print(intx2)
    elif intx1 == x1:
        print(intx1)
    else:
        print(-1)
    
    