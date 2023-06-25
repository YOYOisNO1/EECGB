def program4():
    x, y = map(int, input().split())
    
    r = [y] * 3
    
    i = 0
    
    while r[0] < x:
    
        r[0] = min(r[1]+r[2] - 1, x)
        r.sort()
        i += 1
    print(i)
    
    