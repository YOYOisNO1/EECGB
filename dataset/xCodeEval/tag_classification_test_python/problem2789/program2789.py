def program2789():
    
    import math as ma
    
    n = int(input())
    q = int(ma.sqrt(n))
    
    #primes = array.array('b', )
    
    maxN = 3001
    primes = [0]*maxN
    
    for p in range(2, n+1):
        if (primes[p] == 0):
            for l in range(p, n+1-p, p):
                primes[p+l]+=1
        
    aprimes = len([p for p in range(2, n+1) if primes[p] == 2])
    
    print(aprimes)