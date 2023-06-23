def program3552():
    n = input()
    n = int(n)
    k = 6
    loops = 0
    
    while n >= k:
        n -= k
        k += 6
        loops += 1
    
    pos = [loops * 2, 0]
    
    if n == 0:
        print pos[0], pos[1]
    else: 
        moves = [(1, 2), (-1, 2), (-2, 0), (-1, -2), (1, -2), (2, 0), (1, 2)]
        factors = [loops + 1 for i in range(1, 8)]
        factors[0] = 1
        factors[1] -= 1
    
        j = 0
        while n > 0:
            if factors[j % 7] == 0:
                j += 1
                continue
            for k in range (factors[j % 7]):
                pos[0] += moves[j % 7][0]
                pos[1] += moves[j % 7][1]
                n -= 1
                if (n == 0):
                    break
    
            j += 1
            
        print pos[0], pos[1]