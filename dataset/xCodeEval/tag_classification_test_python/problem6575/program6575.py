def program6575():
    import math
    I=lambda:map(int, input().split())
    n, R, r = I()
    
    if R>=r+r and math.asin(1.0*r/(R-r))*n < 3.1415927:
        print('YES')
    elif n == 1 and r <= R:
        print('YES')
    else:
        print('NO')