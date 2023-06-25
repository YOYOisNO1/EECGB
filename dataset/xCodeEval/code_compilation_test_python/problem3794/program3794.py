def program3794():
    from itertools import permutations
    import sys
    from math import *
    ics, per, first, last = map(int, input().split())
    per = float(per)
    x1 = int(ceil(first / per))
    y1 = int(first % per)
    x2 = int(ceil(last / per))
    y2 = int(last % per)
    
    if x1 == x2:
        print 1
        exit()
    
    if y1 == 1 and y2 == 0:
        print 1
        exit()
        
    if y1 == 1 and last == ics:
        print 1
        exit()
        
    if per == 1:
        print 1
        exit()
        
    if abs(x1-x2) == 1:
        print 2
        exit()
    
    if y1 == 1:
        print 2
        exit()
        
    if y2 == 0:
        print 2
        exit()
        
    if last == ics:
        print 2
        exit()
    
    if y1-y2 == 1 or y2-y1 == per - 1:
        print 2
        exit()
        
    print 3