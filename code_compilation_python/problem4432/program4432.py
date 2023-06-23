    import math
    import sys, os, io
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
def divisor(i):
        s = []
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                s.append(i // j)
                s.append(j)
        return sorted(set(s))
    
def lcm(a, b):
        return a * b // math.gcd(a, b)
    
    n = int(input())
    mod = pow(10, 9) + 7
    ans = 0
    for i in range(2, n):
        c = n - i
        d = divisor(i)
        cnt = [(i - 1) // j for j in d]
        l = len(cnt) - 1
        for j in range(l - 1, -1, -1):
            cj, dj = cnt[j], d[j]
            for k in range(j + 1, l):
                if d[k] % dj:
                    continue
                cj -= cnt[k]
            if cj:
                ans += lcm(dj, c) % mod * cj % mod
                ans %= mod
                cnt[j] = cj
    print(ans)