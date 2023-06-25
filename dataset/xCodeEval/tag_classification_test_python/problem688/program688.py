def program688():
    x1, x2, x3 = (int(x) for x in input().split())
    
    p = max(x1, x2, x3) - min(x1, x2, x3)
    
    print(p)