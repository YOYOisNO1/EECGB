def program5664():
    x, y, n = [ int(x) for x in input().strip().split() ]
    
    a, b = 0, 1
    
    ansA, ansB = a, b
    while b <= n:
        if abs( (b * x - y * a) * ansB * y ) < abs( (ansB * x - y * ansA) * b * y) :
            ansA, ansB = a, b
    
        if x * b <= a * y :
            b += 1
            a = x * b / y
        else:
            a += 1
    
    print("%d/%d") % (ansA, ansB)