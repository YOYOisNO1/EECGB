    #!/usr/bin/env python2
    """
    This file is part of https://github.com/cheran-senthil/PyRival
    Cheran Senthilkumar <hello@cheran.io>
    """
    from __future__ import division, print_function
    
    import os
    import sys
    from atexit import register
    from cStringIO import StringIO
    from itertools import ifilter, imap, izip
    
    range = xrange
    filter, map, zip = ifilter, imap, izip
    
    sys.stdout = StringIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
    input = StringIO(os.read(0, os.fstat(0).st_size)).readline
    
    MOD = 10**9 + 7
    MODF = float(MOD)
    
    MAGIC = 6755399441055744.0
    SHRT = 65536.0
    
    MODF_INV = 1.0 / MODF
    SHRT_INV = 1.0 / SHRT
    
    fround = lambda x: (x + MAGIC) - MAGIC
    fmod = lambda a: a - MODF * fround(MODF_INV * a)
    fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)
    
    
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
        m = int(input())
    
        mu = [-1.0] * (m + 1)
        for i in range(2, m + 1):
            if mu[i] != 0:
                for j in range(2 * i, m + 1, i):
                    mu[j] -= mu[i]
    
        res = 1.0
        for i in range(2, m + 1):
            if mu[i] != 0:
                res = fmul(fmul((m // i), pow(m - m // i, MOD - 2, MOD)), -mu[i], res)
    
        print(int(res) % MOD)
    
    
    if __name__ == '__main__':
        main()