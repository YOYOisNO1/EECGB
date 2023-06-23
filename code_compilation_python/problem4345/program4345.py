def program4345():
    import sys
    
    a, b, m = map(float, sys.stdin.readline().split())
    vx, vy, vz = map(float, sys.stdin.readline().split())
    
    t = -m / vy
    x = a / 2 + t * vx
    z = t * vz
    
    flag = 1;
    while x > a or x < 0:
        if x > a: x -= a
        if x < 0: x += 1
        flag *= -1
    if flag == -1: x = a - x
    
    flag = 1;
    while z > b:
        z -= b
        flag *= -1
    if flag == -1: z = b - z
    
    print x, z
    