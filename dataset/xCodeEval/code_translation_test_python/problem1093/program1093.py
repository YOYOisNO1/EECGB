def program1093():
    import math
    
    x, y, m = input().split(' ')
    x = int(x)
    y = int(y)
    m = int(m)
    
    x, y = min(x, y), max(x, y)
    
    if y >= m:
        print(0)
    elif x + y <= x:
        print(-1)
        
    else: 
        s = int(math.ceil((y - x) / (y * 1.0)))
        
        x += s * y
        while x < y:
            x += y
            s += 1
        
        p = y
        p2 = x
        f = x
        
        
        while f < m:
            f = p2 + p
            p = p2
            p2 = f
            s += 1
        
        print(s)