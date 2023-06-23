def program539():
    a, b, c = map(int, input().split())
    x = a
    y = b
    z = c
    if a > b + c or b > a + c or c > a + b or (a + b + c) % 2 != 0:
        print('Impossible')
        exit(0) 
    if a >= b and a >= c:
        while x <> y + z:
            g += 1
            y -= 1
            z -= 1
        print(x - y, g, x - z)
        exit(0)
    if b >= a and b >= c:
        while y <> x + z:
            g += 1
            x -= 1
            z -= 1
        print(y - x, y - z, g)
        exit(0)
    if c >= a and c >= b:
        while y <> x + z:
            g += 1
            x -= 1
            y -= 1
        print(g, z - y, z - x)
        exit(0)   
        