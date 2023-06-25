def program168():
    
    b, g, n = map(int, input().split())
    _max = max(b, g)
    _min = min(b, g)
    
    if(n<_max):
        print(n+1)
    else:
        print (_min - n + _max + 1)