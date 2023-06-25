def program6576():
    import math
    n, R, r = map(int, input().split())
    R = float(R)
    r = float(r)
    if n == 1:
        if R >= r:
            print('YES')
        else:
            print('NO')
    elif (R-r) * math.sin(math.pi / n) > r - 1.0e-9:
        print('YES')
    else:
        print('NO')