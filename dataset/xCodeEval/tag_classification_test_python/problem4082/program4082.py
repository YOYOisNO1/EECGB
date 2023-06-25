def program4082():
    a = int(input())
    
    r = a%7
    d = a/7
    
    if r == 6:
        mi = (d)*2 + 1
    else:
        mi = d*2
    
    if r >= 2:
        ma = d*2 + 2
    else:
        ma = d*2 + r
    
    print(mi,) ma
        