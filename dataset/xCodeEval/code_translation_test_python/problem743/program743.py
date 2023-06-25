def program743():
    import math
    
    n, t, k, d = map(int, input().split())
    
    s1 = math.ceil(n/k)*t
    
    c = 0
    
    up = 1000*t
    down = 0
    
    while up > down+1:
        mid = (up+down)//2
        c += (mid//t)*k
        c += ((mid-d)//t)*k
        if c>=n:
            up = mid
        else:
            down = mid
        c = 0
    
    c = 0
    ##print('up', up)
    ##print('down', down)
    ##print('mid', mid)
    
    if (down//t)*k + ((down-d)//t)*k == n:
        s2 = down
    elif (mid//t)*k + ((mid-d)//t)*k == n:
        s2 = mid
    else:
        s2 = up
    
    ##print('s1', s1)
    ##print('s2', s2)
    if s2<s1:
        print('YES')
    else:
        print('NO')
    
        
        
        