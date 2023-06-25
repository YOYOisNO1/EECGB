def program4467():
    a, b = map(int, input().split())
    m = 0
    while a > 2 or b > 2:
        while a > 2:
            a -= 2
            b += 1
            m += 1
        while b > 2:
            b -= 2
            a += 1
            m += 1
    if b <= 1 and a <= 1:
        print(m)
    else:
        print(m + 1)
    
    
    
    
    
    
    
    
    
    
    
    