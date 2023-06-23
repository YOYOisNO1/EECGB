def is_visok(x):
        return x % 400 == 0 or x % 4 == 0 and x % 100 != 0
    
    y = int(input())
    
    d, v = 0, is_visok(y)
    year = y
    
    d_ = d
    v_ = not v
    
    while not (v_ == v and d_ % 7 = 0):
        year += 1
        v_ = is_visok(year)
        d_ += (365, 366)[v_] % 7
    
    print(year)