def program4524():
    
    n = int(input())
    
    c = 4
    
    for y in range(1, n-1):
        x = n-1
        if x ** 2 + y ** 2 < n ** 2:
            c += 8
    x = n-1
    y = n-1
    if x ** 2 + y ** 2 < n ** 2 and x + y != 0:
        c += 4
    if n == 0:
        print(1)
    else:
        print(c)