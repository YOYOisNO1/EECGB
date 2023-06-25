    from __future__ import print_function
    import sys
    import math
    import os.path
    import random
    from copy import deepcopy
    from functools import reduce
    from collections import Counter, ChainMap, defaultdict
    from itertools import cycle, chain
    from queue import Queue, PriorityQueue
    from heapq import heappush, heappop, heappushpop, heapify, heapreplace, nlargest, nsmallest
    import bisect
    from statistics import mean, mode, median, median_low, median_high
    # CONFIG
    # LOG 
def log(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)
    # INPUT
def ni():
        return map(int, input().split())
def nio(offset):
        return map(lambda x: int(x) + offset, input().split())
def nia():
        return list(map(int, input().split()))
    # CONVERT
def toString(aList, sep=" "):
        return sep.join(str(x) for x in aList)
def toMapInvertIndex(aList):
        return {k: v for v, k in enumerate(aList)}
    # SORT
def sortId(arr):
        return sorted(range(arr), key=lambda k: arr[k])
    # MATH
def gcd(a,b):
        while b:
            a, b = b, a % b
        return a
    # MAIN
    
    a,b,c,n = ni()
    
    if a >= c and b >= c and a+b-c < n:
        print(n - (a+b-c))
    else:
        print(-1)
        