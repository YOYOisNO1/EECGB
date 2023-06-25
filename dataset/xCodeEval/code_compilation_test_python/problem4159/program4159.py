def program4159():
    import sys
    
    MIN = -1000000000
    x, y, z, k = [int(x) for x in sys.stdin.readline().split()]
    x1, y1, z1 = 1, 1, 1
    for i in range(k):
        a, b, c = MIN, MIN, MIN
        if x1 < x:
            a = (x1+1)*y1*z1
        if y1 < y:
            b = x1*(y1+1)*z1
        if z1 < z:
            c = x1*y1*(z1+1)
        best = max(a, b, c)
        if best == MIN:
            break
        if best == a:
            x1 += 1
        elif best == b:
            y1 += 1
        else:
            z1 += 1
    #print(x1,y1,z1)
    print(x1*y1*z1)