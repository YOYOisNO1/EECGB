def program7491():
    #/usr/bin/python
    # -*- coding: utf-8
    
    a,b,m = map(float,input().split())
    x,y,z = map(float,input().split())
    
    t = m / (-y)
    
    tx = (x*t + a/2.0) % (2*a)
    tz = (z*t) % (2*b)
    
    tx = min(tx, 2*a-tx)
    tz = min(tz, 2*b-tz)
    
    print(tx,) tz