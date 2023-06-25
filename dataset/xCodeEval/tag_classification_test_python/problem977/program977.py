def program977():
    import math
    from collections import deque
    from collections import defaultdict
    
    n = int(input())
    a1,a2,a3 = map(int,input().strip().split(" "))
    b1,b2,b3 = map(int,input().strip().split(" "))
    
    d1,d2,d3 = a1,a2,a3
    e1,e2,e3 = b1,b2,b3
    
    mxa = min(a1,b2) + min(a2,b3) + min(a3, b1)
    
    c4 = min(a1, b1)
    c5 = min(a2, b2)
    c6 = min(a3, b3)
    
    a1 -= c4
    a2 -= c5
    a3 -= c6
    
    c1 = min(b1, a2)
    b1 -= c1
    a2 -= c1
    
    c2 = min(b2,a3)
    b2 -= c2
    a3 -= c2
    
    c3 = min(b3, a1)
    b3 -= c3
    a1 -= c3
    
    # gggggggggggggggggggg
    
    c1 = min(e1, d2)
    e1 -= c1
    d2 -= c1
    
    c2 = min(e2,d3)
    e2 -= c2
    d3 -= c2
    
    c3 = min(e3, d1)
    e3 -= c3
    d1 -= c3
    
    c4 = min(d1, e1)
    c5 = min(d2, e2)
    c6 = min(d3, e3)
    
    e1 -= c4
    e2 -= c5
    e3 -= c6
    
    print(min(a1+a2+a3, e1+e2+e3), mxa)