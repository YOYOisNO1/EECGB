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
    from io import BytesIO
    from string import ascii_lowercase
    
    
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
    
    str_to_num = dict(zip(ascii_lowercase, range(1, 27)))
    
    
def memoize(f):
        """ Memoization decorator for a function taking one or more arguments. """
    
        class memodict(dict):
        def __getitem__(self, *key):
                return dict.__getitem__(self, key)
    
        def __missing__(self, key):
                ret = self[key] = f(*key)
                return ret
    
        return memodict().__getitem__
    
    
def main():
        input()
    
        s = ['']
        for i in input():
            if i != s[-1]:
                s.append(i)
        del s[0]
    
        n = len(s)
    
        @memoize
    def solve(i, j):
            if i == j:
                return 0
    
            res = 1 + solve(i + 1, j)
            for k in range(i + 1, j):
                if s[k] == s[i]:
                    res = min(res, solve(i + 1, k) + solve(k, j))
            return res
    
        print(solve(0, n))
    
    
    if __name__ == '__main__':
        main()