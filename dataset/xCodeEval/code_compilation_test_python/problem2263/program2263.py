    n, k = map(int, input().split())
    a, b = map(int, input().split())
    MOD = n * k
    
def gcd(a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        if a == b:
            return b
        return gcd(b, a % b)
    
    
    x, y = 10 ** 9, 0
    for s in [k + 1 - a, k + 1 + a]:
        for i in range(n):
            t = k * i + 1
    
            el1 = (t - b + MOD) % MOD
            if el1 == 0:
                el1 = MOD
            if el1 - s >= 0:
                l1 = el1 - s
                m = MOD // gcd(l1, MOD)
                x, y = min(x, m), max(y, m)
                # print(s, el1, l1, x, y)
    
            el2 = (t + b + MOD) % MOD
            if el2 == 0:
                el2 = MOD
            if el2 - s >= 0:
                l2 = el2 - s
                m = MOD // gcd(l2, MOD)
                x, y = min(x, m), max(y, m)
                # print(s, el2, l2, x, y)
    
    
    print(x if x != 10 ** 9 else 0, y)
    
    ~                                   