def program5673():
    #! /usr/bin/env python
    #coding=utf-8
    
    
    x, y, n = map(int, input('').split())
    
    dis = 10000000.0
    ansa = 0
    ansb = 0
    value = float(x) / float(y)
    for b in range(1, n + 1):
        a = b * x / y
        if(dis > abs(float((a * y - b * x)) / float(b * y))):
            dis = abs(float((a * y - b * x)) / float(b * y))
            ansa = a
            ansb = b
        a += 1
        if(dis > abs(float((a * y - b * x)) / float(b * y))):
            dis = abs(float((a * y - b * x)) / float(b * y))
            ansa = a
            ansb = b
    print('%d/%d') % (ansa, ansb)
            
            