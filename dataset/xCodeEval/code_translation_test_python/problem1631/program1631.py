def program1631():
    import math
    
    mod = 1000000007
    
    n = int(input())
    res = 0
    phi = list(range(0,n+1))
    
    for i in range(1,n+1):
        for j in range(i*2,n+1,i):
            phi[j] -= phi[i]
    
    phi[1] = 0
    
    for g in range(1,n+1):
        for sum_ab in range(g,n+1,g):
            c = n - sum_ab
            res += g // math.gcd(g,c) * c * phi[sum_ab//g]
            res %= mod
    
    print(res)