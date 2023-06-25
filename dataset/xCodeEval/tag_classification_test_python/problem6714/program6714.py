def solve(n, cache={}):
        if n == 0: return 0
        if n in cache: return cache[n]
    
        v = 0
        while v <= n:
            x = v
            v = v * 10 + 1
            y = v
    
        res1 = (n // x) * len(str(x)) + solve(n % x)
        res2 = len(str(y)) + solve((y - n) % x) + ((y - n) // x) * len(str(x))
        
        cache[n] = min(res1, res2)
        return cache[n]
    
    n = int(input())
    print(solve(n))