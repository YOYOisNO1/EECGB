def program3405():
    from math import *
    
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    print((max(abs(y2-y1),abs(x2-x1))))