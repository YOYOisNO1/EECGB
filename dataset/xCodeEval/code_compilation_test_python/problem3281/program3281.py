def program3281():
    a, b, c, d, e = map(int, input().split())
    
    a //= 1
    
    b //= 1
    
    d //= 7
    
    e //= 4
    
    c //= 2
    
    print(min(a, b, c, d, e))