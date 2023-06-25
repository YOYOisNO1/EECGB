    import sys
    input = sys.stdin.readline
    
    mod = 10**9 + 7
    
def invmod(x, mod):
        return pow(x, mod-2, mod)
    
    a, b, n, x = map(int, input().split())
    if a == 1:
        ans = (pow(a, n, mod) * x + b * n) % mod
    else:
        ans = pow(a, n, mod) * x + b * (pow(a, n, mod) - 1 + mod) * invmod(a-1, mod)
        ans %= mod
    print(ans)