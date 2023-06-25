def program5663():
    from math import *
    from fractions import *
    
    x,y,n = map(int, input().split())
    integer_part = x/y
    x -= integer_part*y
    y *= 1.0
    
    l = []
    for denom in xrange(1,n+1):
      a = int(floor(x*denom/y))
      b = int(ceil (x*denom/y))
      l.append((a,denom))
      l.append((b,denom))
    
    a,b = min(l, key=lambda t: (abs((x*t[1]-y*t[0])/(t[1]*y)),t[1],t[0]))
    print("%d/%d")%(integer_part*b+a,b)