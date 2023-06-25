    import sys
    
def powmod(a, b, m):
        if b <= 30:
            return a ** b % m
        else:
            return powmod(powmod(a, 30, m), b/30, m) * (a ** (b % 30) % m) % m
    
    
    n = int(sys.stdin.readline())
    m = 1000000007
    
    if n == 0:
        print(1)
    else:
        # ans = 2 ** n + 2 ** (2*n - 1)
        ans = powmod(2, n - 1, m)
        ans += powmod(2, 2 * n - 1, m)
        ans %= m
        print(ans)