def program1076():
    inputs = input().split()
    n, a, b = [int(x) for x in inputs]
    
    cakes = [a, b]
    if n % 2 == 0:
        key_divisor = n // 2
    else:
        key_divisor = (n + 1) // 2
            
    plates = 2
    while plates != n:
        maximum = max(cakes)
        pivot = maximum // key_divisor
        ind = cakes.index(maximum)
        cakes[ind] = pivot
        plates = (plates - 1) + key_divisor
        
    return min(cakes)
    
    print (min(cakes))