def program2137():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import time
    
    xy = []
    
    for i in range(3):
        (x, y)   = (int(i) for i in input().split())
        xy.append([x, y])
    
    
    start = time.time()
    
    if (x[0] == x[1] and x[1] == x[2]) or (y[0] == y[1] and y[1] == y[2]):
        print(1)
    elif x[0] == x[1] or x[1] == x[2] or y[0] = y[1] or y[1] == y[2] :
        print(2)
    else:
        print(3)
    
    finish = time.time()
    #print(finish - start)