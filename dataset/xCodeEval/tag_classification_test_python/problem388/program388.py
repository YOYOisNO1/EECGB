def program388():
    n, a, b, c = map(int, input().split())
    
    delta = 4 - (n % 4)
    
    if delta == 4:
        print(0)
    
    if delta == 1:
        if a < c * 3:
            if a < b + c:
                print(a)
            else:
                print(b) + c
        else:
            if c * 3 < b + c:
                print(c) * 3
            else:
                print(b) + c
    
    if delta == 2:
        if a + a < b:
            if a + a < c * 2:
                print(a) + a
            else:
                print(c) * 2
        else:
            if b < c * 2:
                print(b)
            else:
                print(c) * 2
    
    if delta == 3:
        if a * 3 < b + a:
            if a * 3 < c:
                print(a) * 3
            else:
                print(c)
        else:
            if b + a < c:
                print(b) + a
            else:
                print(c)