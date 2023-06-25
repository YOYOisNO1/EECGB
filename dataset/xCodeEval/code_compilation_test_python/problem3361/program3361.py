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
        from math import gcd
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
    
    def gcd(x, y):
            """gcd(x, y) -> int
            greatest common divisor of x and y
            """
            while y:
                x, y = y, x % y
            return x
    
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
    
    
def main():
        n, m, l = map(int, input().split(' '))
        a = list(map(int, input().split(' ')))
        points_to_cut = [1 if i > l else 0 for i in a]
    
        starts, ends = set(), set()
        if points_to_cut[0] == 1:
            starts.add(0)
    
        for i, pi in enumerate(points_to_cut):
            if i == 0:
                continue
            if pi == 0:
                if points_to_cut[i - 1] == 1:
                    ends.add(i - 1)
            if pi == 1:
                if points_to_cut[i - 1] == 0:
                    starts.add(i)
    
        if points_to_cut[-1] == 1:
            ends.add(n - 1)
    
        for _ in range(m):
            q = list(map(int, input().split(' ')))
            if q[0] == 0:
                print(len(starts))
            else:
                a[q[1] - 1] += q[2]
                if a[q[1] - 1] > l:
                    if points_to_cut[q[1] - 1] == 0:
                        if (q[1] in starts) and ((q[1] - 2) in ends):
                            starts.remove(q[1])
                            ends.remove(q[1] - 2)
                        elif q[1] in starts:
                            starts.remove(q[1])
                            starts.add(q[1] - 1)
                        elif (q[1] - 2) in ends:
                            ends.remove(q[1] - 2)
                            ends.add(q[1] - 1)
                        else:
                            starts.add(q[1] - 1)
                            ends.add(q[1] - 1)
    
                        points_to_cut[q[1] - 1] = 1
    
    
    if __name__ == '__main__':
        sync_with_stdio(False)
    
        if 'PyPy' in sys.version:
            from _continuation import continulet
    
        def bootstrap(c):
                callable, arg = c.switch()
                while True:
                    to = continulet(lambda _, f, x: f(x), callable, arg)
                    callable, arg = c.switch(to=to)
    
            c = continulet(bootstrap)
            c.switch()
    
            main()
    
        else:
            import threading
    
            sys.setrecursionlimit(2097152)
            threading.stack_size(134217728)
    
            main_thread = threading.Thread(target=main)
            main_thread.start()
            main_thread.join()