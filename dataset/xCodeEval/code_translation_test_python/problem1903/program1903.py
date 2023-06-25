def program1903():
    a, b, m = input().split()
    x, y, z = input().split()
    a, b, m = float(a), float(b), float(m)
    x, y, z = float(x), float(y), float(z)
    
    t = -m / y
    p = a / 2 + x * t
    q = z * t
    
    
    while p > a or p < 0:
        if p > a:
            p = a * 2 - p
        else:
            p = -p
    
    while q > b or q < 0:
        if q > b:
            q = b * 2 - q
        else:
            q = -q
    
    print("%.10lf %.10lf" % (p, q))