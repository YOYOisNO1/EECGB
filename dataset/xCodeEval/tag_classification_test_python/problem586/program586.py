def program586():
    from sys import exit
    
    read = input
    
    readints = lambda: map(int, read().split())
    
    x, y, z = readints()
    x1, y1, z1 = readints()
    a = readints()
    
    t = range(6)
    t[0] = y < 0
    t[1] = y > y1
    t[2] = z < 0
    t[3] = z > z1
    t[4] = x < 0
    t[5] = x > x1
    
    print(reduce(lambda) a, b: a + b, [a[i] if t[i] else 0 for i in range(6)])
    