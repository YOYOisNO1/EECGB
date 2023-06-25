def exp(base,power,MOD,store):
        if store[power] != -1:
            return store[power]
    
        if power == 0:
            return 1
    
        if power % 2 == 0:
            store[power] = ((exp(base,power/2,MOD,store))**2) % MOD
        else:
            store[power] = (base *((exp(base,power/2,MOD,store))**2)) % MOD
        return store[power]
    
        
    
        
    p,k = map(int,input().split())
    MOD = 1000000007
    
    if k == 0:
        store = [-1] * (p+1)
        ans = exp(p,p-1,MOD,store) % MOD
    elif k == 1:
        store = [-1] * (p+1)
        ans = exp(p,p,MOD,store) % MOD
    else:
    
        x = k
        times = 1
    
        while x !=1:
            x = (x * k) % p
            times += 1
            if times > (p-1)/2:
                times = p-1
                break
    
    
        groups = (p-1) / times
        store = [-1] * (groups+1)
        ans = exp(p,groups,MOD,store) % MOD
    
    print(ans)