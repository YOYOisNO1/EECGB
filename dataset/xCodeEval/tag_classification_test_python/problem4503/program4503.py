def program4503():
    import sys
    input = lambda: sys.stdin.readline().rstrip()
    from collections import Counter
     
    mod = 998244353
    import math
    n,m = map(int,input().split())
     
    '''
    1 1
    1 2
    1 3 
    2 1
    2 2
    2 3
    3 1 - amb
    3 2 - non
    3 3 - amb
     
    1 2 4
    1 2 6 
     
    6 + 18 + 36 + 36
    1 2
      2,4,6 3,6
      
    2 2 6 6
    2 6 4
     
     
     
    2 1 1 1
    1 1 1 1
    1 2
    2 2
    1
    2
     
    '''
     
    #print(6*6*6*6 + 6*6*6 + 6*6 + 6 - 1494, '60')
    #print(16 + 8 + 4 + 2)
     
    x = m
    y = m
     
    t = y - x
    g = 1
     
    primes = []
     
    for i in range(2, 10**4):
        ok = 1
        for j in range(2,103):
            if j<i and i%j==0:
                ok = 0
                break
        if ok:
            primes.append(i)
            
    primes = set(primes)
     
    for j in range(1,n):
        if g<= m:
            if j+1 in primes:
                g *= j+1
        
        y *= m
        y = y % mod
        
        t += y
        t = t % mod
        
        if g <=m:
            x *= m//g
            
            t -= x
        
    print(t%mod)
       