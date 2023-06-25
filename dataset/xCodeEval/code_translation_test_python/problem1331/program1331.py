    import gc
    import heapq
    import itertools
    import math
    import sqlite3
    from collections import Counter, deque, defaultdict
    from sys import stdout
    import time
    from math import factorial, log, gcd
    import sys
    from decimal import Decimal
    import threading
    from heapq import *
    from fractions import Fraction
    
    
def S():
        return sys.stdin.readline().split()
    
    
def I():
        return [int(i) for i in sys.stdin.readline().split()]
    
    
def II():
        return int(sys.stdin.readline())
    
    
def IS():
        return sys.stdin.readline().replace('\n', '')
    
    
def main():
        n, a = I()
    
        m = [(float('inf'), -1) for _ in range(n + 10)]
        queue = deque([(a, 0)])
        m[len(str(a))] = (0, a)
        _dict = defaultdict(bool)
        _dict[a] = True
        while queue:
            c, q = queue.pop()
            for d in set(str(c)):
                if int(d) > 1:
                    new_c = c * int(d)
                    str_c = str(new_c)
                    if m[len(str_c)][0] > q + 1:
                        m[len(str_c)] = (q + 1, new_c)
                    _set = [int(i) for i in str_c]
                    if not (max(_set) < 2 or len(str_c) >= n or _dict[new_c]):
                        _dict[new_c] = True
                        queue.appendleft((new_c, q + 1))
    
        print(m[n][0] if m[n][0] < float('inf') else -1)
    
    
    if __name__ == '__main__':
        # for _ in range(II()):
        #     main()
        main()