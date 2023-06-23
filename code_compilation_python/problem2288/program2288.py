def program2288():
    ﻿x = input()
    y = input() 
    z = input()
    t1 = input()
    t2 = input()
    t3 = input()
    
    me = x - y
    
    if me < 0:
    	me = me * (-1)
    
    run = me * t1
    
    ml = x - z
    
    if ml < 0:
    	ml = ml * (-1)
    
    lift = ml * t2 + me * t2 + 2 * t3
    
    if lift <= run:
    	print("YES")
    else:
    	print("NO")