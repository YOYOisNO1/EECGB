def add(a, b, mod):
        return (a + b) % mod
def mul(a, b, mod):
        return (a * b) % mod
def sub(a, b, mod):
        return (a - b + mod) % mod
def binpow(a, n, mod):
        if n == 0:
            return 1
        if n % 2 == 1:
            return mul(a, binpow(a, n - 1, mod), mod)
        b = binpow(a, n // 2, mod)
        return mul(b, b, mod)
def prime(n):
        for i in range(2, int((n ** 0.5)) + 1):
            if n % i == 0:
                return False
        return n > 1
    MOD = 998244353
    n, m = map(int, input().split())
    p = 1
    ans = 0
    cur = m
    ans = sub(ans, cur, MOD)
    for i in range(1, n + 1):
        ans = add(ans, int(pow(m, i, MOD)), MOD)
    for i in range(1, n):
        if prime(i + 1):
            p *= (i + 1)
        if p > m:
            break
        cur = mul(cur, m // p, MOD)
        ans = sub(ans, cur, MOD)
    print(ans)