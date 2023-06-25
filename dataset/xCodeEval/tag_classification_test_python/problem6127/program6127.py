def program6127():
    r1, c1, r2, c2 = map(int, input().split())
    a = 0
    b = 0
    c = max(abs(r2 - r1), abs(c2 - c1))
    
    if r1 == r2 or c1 == c2:
        a = 1
    else:
        a = 2
    
    if r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2:
        b = 1
    elif (r1 + c1) % 2 != (r2 + c2) % 2:
        b = 0
    else:
        b = 2
    
    print(a, b, c)