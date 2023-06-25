def power(x, y, p) : 
        res = 1 
        x = x % p  
        if (x == 0) : 
            return 0
        while (y > 0) : 
            if ((y & 1) == 1) : 
                res = (res * x) % p 
            y = y >> 1
            x = (x * x) % p 
              
        return res 
    n, m = [int(p) for p in input().split()]
    mod = 10**9+7
    
    temp = power(2, m, mod)
    temp -= 1%mod
    temp = temp%mod
    ans = power(temp, n, mod)
    print(ans)