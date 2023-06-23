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
        init_w = int(input())
        cnt = [int(i) for i in input().split()]
    
        dp_cnt = [min(cnt_i, 16) for i, cnt_i in enumerate(cnt)]
        greedy_cnt = [cnt_i - dp_cnt_i for cnt_i, dp_cnt_i in zip(cnt, dp_cnt)]
    
        i, w = 8, init_w
        while (i > 0) and (w > 0):
            w -= i * greedy_cnt[i - 1]
            if w < 0:
                w %= i
                for j in range(2):
                    w += i if min(greedy_cnt[i - 1], dp_cnt[i - 1]) > j + 1 else 0
    
            i -= 1
    
        weights = reduce(list.__add__, (dp_cnt_i * [i + 1] for i, dp_cnt_i in enumerate(dp_cnt)))
    
        @memoize
    def solve(i, val):
            if val == 0:
                return True
            if i == 0:
                return False
            return solve(i - 1, val) or solve(i - 1, val - weights[i - 1])
    
        for val in range(min(w, sum(weights)), -1, -1):
            if solve(len(weights), val):
                print(init_w - w + val)
                break
    
    
    if __name__ == '__main__':
        main()