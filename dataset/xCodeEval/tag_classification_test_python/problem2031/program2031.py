    __author__ = 'd555_'
    db = False
    MOD = 1000000007
    
    if db:
        import sys
        sys.stdin = open("input.txt", "r")
    
    
    n, k, d = map(int, input().split())
    
    dp = dict()
    
    
def f(n, x):
        if db:
            print("f"),(n,x)," ->"
        if (n, x) in dp:
            if db: print(dp[(n,x)],) " con ", (n,x)
            return dp[(n, x)]
        if n == 0:
            if db: print("n=0"), (n,x) ,"=>", (d <= x <= k)
            dp[(0, x)] = (d <= x <= k)
            return d <= x <= k
        if n < 0:
            if db: print("n<0"), (n,x)
            dp[(n, x)] = 0
            return 0
        c = 0
        for i in range(1, k+1):
            c += f(n - i, max(x, i)) if n - i >= 0 else 0
            if not db:
                c %= MOD
        dp[(n, x)] = c % MOD
        return c % MOD
    
    if db: print(dp)
    print(f(n,) 0)