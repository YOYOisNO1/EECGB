def program1545():
    
    [p, d] = [int(x) for x in input().split()]
    
    
    base = 10
    
    
    best_number = p
    
    for i in range(0,18):
        r = (p%base)+1
        # print(r)
        if r != base and r <= d:
            best_number = p-r
        base *= 10
    
    print(best_number)