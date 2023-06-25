def program4526():
    
    n = int(input())
    c = 4
    if n == 0:
        c = 1
    
    for x in [-n+1, n-1]:
        for y in [-n + 1, n - 1]:
            if y == 0 and x == 0:
                continue
            if x**2+y**2 < n**2:
                c += 1
    
    for x in [-n+1, n-1]:
        for y in range(-n+2, n-1):
            if y == 0 or x == 0:
                continue
            if x**2+y**2 < n**2:
                c += 1
    
    for y in [-n+1, n-1]:
        for x in range(-n+2, n-1):
            if y == 0 or x == 0:
                continue
            if x**2+y**2 < n**2:
                c += 1
    
    print(c)