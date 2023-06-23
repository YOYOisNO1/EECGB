    #!/usr/bin/env python
    """
    This file is part of https://github.com/Cheran-Senthil/PyRival.
    
    Copyright 2018 Cheran Senthilkumar all rights reserved,
    Cheran Senthilkumar <hello@cheran.io>
    Permission to use, modify, and distribute this software is given under the
    terms of the MIT License.
    
    """
    from __future__ import division, print_function
    
    import itertools
    import random
    import sys
    from atexit import register
    from collections import Counter
    
    if sys.version_info[0] < 3:
        from io import BytesIO as stream
    else:
        from io import StringIO as stream
    
    
    if sys.version_info[0] < 3:
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
    
        input = input
        range = xrange
    
        filter = itertools.ifilter
        map = itertools.imap
        zip = itertools.izip
    
    
def sync_with_stdio(sync=True):
        """Set whether the standard Python streams are allowed to buffer their I/O.
    
        Args:
            sync (bool, optional): The new synchronization setting.
    
        """
        global input, flush
    
        if sync:
            flush = sys.stdout.flush
        else:
            sys.stdin = stream(sys.stdin.read())
            input = lambda: sys.stdin.readline().rstrip('\r\n')
    
            sys.stdout = stream()
            register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
    
    
def gcd(x, y):
        """greatest common divisor of x and y"""
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
    
    
def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True
    
    
def is_prime(n):
        """
        Deterministic variant of the Miller-Rabin primality test to determine
        whether a given number is prime.
    
        Parameters
        ----------
        n : int
            n >= 0, an integer to be tested for primality.
    
        Returns
        -------
        bool
            False if n is composite, otherwise True.
        """
        if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            return True
    
        if (any((n % p) == 0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])) or (n in [0, 1]):
            return False
    
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
    
        if n < 2047:
            return not _try_composite(2, d, n, s)
        if n < 1373653:
            return not any(_try_composite(a, d, n, s) for a in [2, 3])
        if n < 25326001:
            return not any(_try_composite(a, d, n, s) for a in [2, 3, 5])
        if n < 118670087467:
            if n == 3215031751:
                return False
            return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7])
        if n < 2152302898747:
            return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11])
        if n < 3474749660383:
            return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13])
        if n < 341550071728321:
            return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17])
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23])
    
    
def _factor(n):
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if n % i == 0:
                return i
    
        y, c, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
        g, r, q = 1, 1, 1
    
        while g == 1:
            x = y
            for i in range(r):
                y = ((y * y) % n + c) % n
            k = 0
            while (k < r) and (g == 1):
                ys = y
                for i in range(min(m, r - k)):
                    y = ((y * y) % n + c) % n
                    q = q * (abs(x - y)) % n
                g = gcd(q, n)
                k = k + m
            r = r * 2
    
        if g == n:
            while True:
                ys = ((ys * ys) % n + c) % n
                g = gcd(abs(x - ys), n)
                if g > 1:
                    break
    
        return g
    
    
    @memodict
def factors(n):
        """
        Integer factorization using Pollard's rho algorithm.
    
        Parameters
        ----------
        n : int
            n > 1, an integer to be factorized.
    
        Returns
        -------
        Counter
            Counter of the prime factors of n.
        """
        if is_prime(n):
            return Counter([n])
        else:
            f = _factor(n)
            if f == n:
                return factors(n)
            else:
                return factors(f) + factors(n//f)
    
    
def main():
        n, k = map(int, input().split(' '))
    
        if n == 1:
            print(1)
            return
    
        res = 1
        for p, x in factors(n).items():
            if k == 0:
                res = (res * pow(p, x, 1000000007)) % 1000000007
            else:
                dp = [[1] * (x + 1) for _ in range(k + 1)]
    
                for i in range(1, k + 1):
                    if i == 0:
                        for j in range(1, x + 1):
                            dp[0][j] = (dp[0][j - 1] * p) % 1000000007
                    else:
                        for j in range(x + 1):
                            if j == 0:
                                dp[i][j] = dp[i - 1][0]
                            else:
                                dp[i][j] = (((dp[i][j - 1] * j) + dp[i - 1][j]) *
                                            pow(j + 1, 1000000005, 1000000007)) % 1000000007
    
                res = (res * dp[k][x]) % 1000000007
    
        print(res)
        return
    
    
    if __name__ == '__main__':
        sync_with_stdio(False)
        main()