    #!/usr/bin/env python2
    """
    This file is part of https://github.com/cheran-senthil/PyRival
    Copyright 2019 Cheran Senthilkumar <hello@cheran.io>
    
    """
    from __future__ import division, print_function
    
    import itertools
    import math
    import os
    import sys
    from atexit import register
    from io import BytesIO
    
    
    class dict(dict):
        """dict() -> new empty dictionary"""
    
    def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
    
    def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
    
    def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
    
    
def gcd(x, y):
        """greatest common divisor of x and y"""
        while y:
            x, y = y, x % y
        return x
    
    
    range = xrange
    
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
    
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
    
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    
    MOD = 998244353
    MODF = float(MOD)
    SHRT = float(1 << 16)
    ROOT = 3.0
    
    fmod = lambda x: x - MODF * math.trunc(x / MODF)
    fmul = lambda a, b: fmod(math.trunc(a / SHRT) * fmod(b * SHRT) + (a - SHRT * math.trunc(a / SHRT)) * b)
    
    
def fpow(x, y):
        res = 1.0
        while y > 0:
            if y & 1 == 1:
                res = fmul(res, x)
            if y > 1:
                x = fmul(x, x)
            y >>= 1
    
        return res
    
    
def ntt(a, inv=False):
        n = len(a)
        w = [1.0] * (n >> 1)
    
        w[1] = fpow(ROOT, (MOD - 1) // n)
        if inv:
            w[1] = fpow(w[1], MOD - 2)
    
        for i in range(2, (n >> 1)):
            w[i] = fmul(w[i - 1], w[1])
    
        rev = [0] * n
        for i in range(n):
            rev[i] = rev[i >> 1] >> 1
            if i & 1 == 1:
                rev[i] |= (n >> 1)
            if i < rev[i]:
                a[i], a[rev[i]] = a[rev[i]], a[i]
    
        step = 2
        while step <= n:
            half, diff = step >> 1, n // step
            for i in range(0, n, step):
                pw = 0
                for j in range(i, i + half):
                    v = fmul(w[pw], a[j + half])
                    a[j + half] = a[j] - v
                    a[j] += v
                    pw += diff
    
            step <<= 1
    
        if inv:
            inv_n = fpow(n, MOD - 2)
            for i in range(n):
                a[i] = fmul(a[i], inv_n)
    
    
def conv(a, b):
        s = len(a) + len(b) - 1
        n = 1 << s.bit_length()
    
        a.extend([0.0] * (n - len(a)))
        b.extend([0.0] * (n - len(b)))
    
        ntt(a)
        ntt(b)
    
        for i in range(n):
            a[i] = fmul(a[i], b[i])
    
        ntt(a, inv=True)
        del a[s:]
    
    
def main():
        n, _ = map(int, input().split())
        n >>= 1
    
        d = [0.0] * 2097152
        for i in map(int, input().split()):
            d[i] = 1.0
    
        ntt(d)
        d = [fpow(i, n) for i in d]
        ntt(d, inv=True)
    
        print(int(sum(fmul(i, i) for i in d) % MODF))
    
    
    if __name__ == '__main__':
        main()