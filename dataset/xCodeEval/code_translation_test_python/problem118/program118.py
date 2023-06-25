def program118():
    # map(int, input().split())
    
    a, b, c, d = map(int, input().split())
    
    count = 0
    
    if a <= b <= c:
    
        v1 = a
    
        v2 = b
    
        v3 = c
    
    elif a <= c <= b:
    
        v1 = a
    
        v2 = c
    
        v3 = b
    
    elif b <= a <= c:
    
        v1 = b
    
        v2 = a
    
        v3 = c
    
    elif b <= c <= a:
    
        v1 = b
    
        v2 = c
    
        v3 = a
    
    elif c <= a <= b:
    
        v1 = c
    
        v2 = a
    
        v3 = b
    
    else:
    
        v1 = c
    
        v2 = b
    
        v3 = a
    
    count = 0
    
    if v3-v2 < d:
    
        count += d-(v3-v2)
    
    if v2-v1 < d:
    
        count += d-(v2-v1)
    
    print(count)