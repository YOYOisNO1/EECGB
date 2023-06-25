    from sys import stdin
    
    mod = 10**9+7
    
def geo(x, n, m):
        return (pow(x, n+1, m) - 1)*pow(x-1, m-2, m)
    
    p, q, n, a = [int(x) for x in stdin.readline().rstrip().split()]
    if p <= 1:
        print((a + q * n) % mod)
    else:
        ans = (a * pow(p, n, mod) + q * (geo(p, n-1, mod) % mod)) % mod
        print(ans)