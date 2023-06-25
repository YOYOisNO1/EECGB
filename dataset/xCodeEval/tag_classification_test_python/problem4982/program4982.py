    #!/usr/bin/env python2
    """
    This file is part of https://github.com/cheran-senthil/PyRival
    Copyright 2019 Cheran Senthilkumar <hello@cheran.io>
    
    """
    from __future__ import division, print_function
    
    import itertools
    import os
    import sys
    from atexit import register
    from collections import Counter
    from io import BytesIO
    from random import randint
    
    range = xrange
    
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
    
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
    
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    
    
def gcd(x, y):
        """ greatest common divisor of x and y """
        while y:
            x, y = y, x % y
        return x
    
    
def memodict(f):
        """ Memoization decorator for a function taking a single argument. """
    
        class memodict(dict):
        def __missing__(self, key):
                ret = self[key] = f(key)
                return ret
    
        return memodict().__getitem__
    
    
def memoize(f):
        """ Memoization decorator for a function taking one or more arguments. """
    
        class memodict(dict):
        def __getitem__(self, *key):
                return dict.__getitem__(self, key)
    
        def __missing__(self, key):
                ret = self[key] = f(*key)
                return ret
    
        return memodict().__getitem__
    
    
    @memodict
def pollard_rho(n):
        if n == 1:
            return Counter()
    
        d, s = n - 1, 0
        while not d & 1:
            d, s = d >> 1, s + 1
    
    def try_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n - 1:
                    return False
            return True
    
        if not any(try_composite(w) for w in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]):
            return Counter({n: 1})
    
        y, c, m = randint(1, n - 1), randint(1, n - 1), randint(1, n - 1)
        g, r, q = 1, 1, 1
    
        while g == 1:
            x, k = y, 0
    
            for _ in range(r):
                y = (y * y + c) % n
    
            while (k < r) and (g == 1):
                ys = y
    
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    q = (q * abs(x - y)) % n
    
                g = gcd(q, n)
                k += m
    
            r *= 2
    
        if g == n:
            while True:
                ys = (ys * ys + c) % n
                g = gcd(abs(x - ys), n)
                if g > 1:
                    break
    
        return pollard_rho(g) + pollard_rho(n // g)
    
    
    @memodict
def prime_factors(n):
        """ Prime factorization using Pollard's rho algorithm. """
        factors = Counter()
    
        for p in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837]:
            if n % p == 0:
                cnt = 0
                while n % p == 0:
                    n, cnt = n // p, cnt + 1
                factors[p] = cnt
    
        return factors + pollard_rho(n)
    
    
    MOD = 10**9 + 7
    MODF = float(MOD)
    
    MAGIC = 6755399441055744.0
    SHRT = 65536.0
    
    MODF_INV = 1.0 / MODF
    SHRT_INV = 1.0 / SHRT
    
    fround = lambda x: (x + MAGIC) - MAGIC
    fmod = lambda a: a - MODF * fround(MODF_INV * a)
    fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)
    
    
    @memoize
def fpow(x, y):
        if y == 0:
            return 1.0
    
        res = 1.0
        while y > 1:
            if y & 1 == 1:
                res = fmul(res, x)
            x = fmul(x, x)
            y >>= 1
    
        return fmul(res, x)
    
    
def main():
        n, k = map(int, input().split())
    
        if n == 1:
            print(1)
            return
    
        res = 1.0
        for p, x in prime_factors(n).items():
            dp = [1.0] * (x + 1)
            for i in range(1, x + 1):
                dp[i] = fmul(dp[i - 1], p)
    
            for i in range(1, k + 1):
                _dp = [1.0] * (x + 1)
                for j in range(1, x + 1):
                    _dp[j] = fmul(fmul(_dp[j - 1], j, dp[j]), fpow(j + 1, MOD - 2))
                dp = _dp
    
            res = fmul(res, dp[x])
    
        print(int(res) % MOD)
    
    
    if __name__ == '__main__':
        main()