    #!/usr/bin/env python
    """
    This file is part of https://github.com/Cheran-Senthil/PyRival.
    
    Copyright 2018 Cheran Senthilkumar all rights reserved,
    Cheran Senthilkumar <hello@cheran.io>
    Permission to use, modify, and distribute this software is given under the
    terms of the MIT License.
    
    """
    from __future__ import division, print_function
    
    import cmath
    import itertools
    import math
    import operator as op
    # import random
    import sys
    from atexit import register
    from bisect import bisect_left, bisect_right
    # from collections import Counter, MutableSequence, defaultdict, deque
    # from copy import deepcopy
    # from decimal import Decimal
    # from difflib import SequenceMatcher
    # from fractions import Fraction
    # from heapq import heappop, heappush
    
    if sys.version_info[0] < 3:
        # from cPickle import dumps
        from io import BytesIO as stream
        # from Queue import PriorityQueue, Queue
    else:
        # from functools import reduce
        from io import StringIO as stream
        # from pickle import dumps
        # from queue import PriorityQueue, Queue
    
    
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
    
    
def main():
        n, k = map(int, input().split(' '))
        n //= 2
    
        inv = [1] * (9*n + 2)
        for i in range(2, 9*n + 2):
            inv[i] = -inv[998244353 % i] * (998244353 // i) % 998244353
    
        a = list(map(int, input().split(' ')))
        mi = min(a)
    
        a = list(map(lambda x: x - mi, a))
        a.remove(0)
    
        b = [0] * 16
        b[0] = 1
    
        ans = 0
        for i in range(9*n + 1):
            ans += b[i & 15] * b[i & 15]
            if ans >= 7971934306371108872:
                ans -= 7971934306371108872
    
            s = 0
            for x in a:
                s += b[(i - x + 17) & 15] * (n * x - (i - x + 1))
            b[(i + 1) & 15] = s % 998244353 * inv[i + 1] % 998244353
    
        print(ans % 998244353)
    
    
    if __name__ == '__main__':
        sync_with_stdio(False)
        main()