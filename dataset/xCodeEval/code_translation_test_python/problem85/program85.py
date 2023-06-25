def program85():
    n = int(input())
    
    base = 3
    if n == 1:
        print(base)
    else:
        krug = n // base
        if n % base == 2:
            krug += 1 
        
        res = 5
        res += (krug - 1) * 4
        if n % base == 0:
            res += 2
        elif n % base == 1:
            res += 3
        
        print(res)