    import sys
    from functools import lru_cache
    
    GAP = MOD = 998244353
    
    # 阶乘
    factorial_save = [1, 1]
    
    for i in range(2, 11000):
        x = factorial_save[i - 1]
        x *= i
        x %= GAP
        factorial_save.append(x)
    
    @lru_cache
def ncm1(n, m):
        '''组合数逆元取模'''
        a = factorial_save[n]
        b = pow(factorial_save[m], GAP - 2)
        c = pow(factorial_save[n-m], GAP - 2)
        return a * b * c % GAP
    
    @lru_cache
def ncm2(n, m):
        '''组合数顺次取模'''
        if m * 2 > n:
            m = n - m
        r = 1
        for i in range(m):
            r *= (n - i) / (m - i)
        r = int(round(r))
        return r % GAP
    
    @lru_cache
def ncm(n, m):
        '''组合数取模'''
        if n <= 400 or m <= 100 or n - m <= 100:
            return ncm2(n, m)
        return ncm1(n, m)
    
    @lru_cache
def f(n, x):
        if n == 0:
            return 1
        if n == 1:
            return 0
        if n == 2:
            return x
        if x <= n - 1:
            return pow(x, n, MOD)
        res = 0
        for m in range(0, n + 1):
            res += ncm(n, m) * pow(n - 1, n - m, MOD) * f(m, x - n + 1)
            res %= MOD
        return res
    
    n, x = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    print(f(n, x))
    