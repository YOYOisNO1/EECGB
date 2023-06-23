def program1026():
    from math import *
    life = 100
    (x, y) = map(float, input().split())
    r = (sqrt(x**2 + y**2))
    t = atan(y / x) > 0
    print 'white' if int(r) % 2 == 0 ^ t and r != int(r) else 'black'