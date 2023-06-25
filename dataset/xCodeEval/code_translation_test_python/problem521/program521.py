    import re
    import sys
    from bisect import bisect, bisect_left, insort, insort_left
    from collections import Counter, defaultdict, deque
    from copy import deepcopy
    from decimal import Decimal
    from itertools import (
        accumulate, combinations, combinations_with_replacement, groupby,
        permutations, product)
    from math import (acos, asin, atan, ceil, cos, degrees, factorial, gcd, hypot,
                      log2, pi, radians, sin, sqrt, tan)
    from operator import itemgetter, mul
    from string import ascii_lowercase, ascii_uppercase, digits
    
    
def inp():
        return(int(input()))
    
    
def inlist():
        return(list(map(int, input().split())))
    
    
def instr():
        s = input()
        return(list(s[:len(s)]))
    
    
def invr():
        return(map(int, input().split()))
    
    
    x, y, z = invr()
    a = int(sqrt((x*z)/y))
    c = z//a
    b = y//c
    print(a*4+b*4+c*4)