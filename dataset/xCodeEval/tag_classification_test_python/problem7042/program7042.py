def program7042():
    import math
    
    n     = int(input())
    level = 1
    r     = [0,0,1,3]
    cnt   = 0
    
    while level <= n:
        num  = math.ceil(n/level)
        d_   = num // 4 
        r_   = num % 4
        
        cnt += d_    * level * 4
        cnt += r[r_] * level 
        
        level *= 4
        
    print(cnt)    