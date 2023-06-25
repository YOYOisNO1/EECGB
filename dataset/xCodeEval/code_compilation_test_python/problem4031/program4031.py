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
    
    
def get_primes(n):
        """ Input n>=6, Returns a generator of primes, 5 <= p < n """
        sieve = bytearray((n // 3 + (n % 6 == 2) >> 3) + 1)
    
        for i in range(1, int(n**0.5) // 3 + 1):
            if not (sieve[i >> 3] >> (i & 7)) & 1:
                k = (3 * i + 1) | 1
                for j in range(k * k // 3, n // 3 + (n % 6 == 2), 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
                for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + (n % 6 == 2), 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
    
        return (3 * i + 1 | 1 for i in range(1, n // 3 + (n % 6 == 2)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    
    
def main():
        m = int(input())
        if m == 1:
            print(1)
        else:
            res = 2.0
            if m >= 3:
                res = fmod(res + fpow(3, MOD - 2))
            for p in get_primes(m + 1):
                res = fmod(res + fpow(p, MOD - 2))
    
            print(int(res) % MOD)
    
    
    if __name__ == '__main__':
        main()