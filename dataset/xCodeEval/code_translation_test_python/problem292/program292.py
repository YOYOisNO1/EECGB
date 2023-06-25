def program292():
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import sys
    import math
    import random
    import operator
    from fractions import Fraction, gcd
    from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations
    getcontext().prec = 100
    
    MOD = 10**9 + 7
    INF = float("+inf")
    
    n, m = map(int, input().split())
    halflen = n /2
    
    arr = [None] * n
    i = 0
    j = n - 1
    
    for x in xrange(n):
        nn = n - x - 2
        # print("x m nn"), x, m, nn
        if m > 2**nn:
            # print("last")
            arr[j] = x + 1
            j -= 1
            m -= 2**nn
        else:
            # print("first")
            arr[i] = x + 1
            i += 1
    
    # bm = bin(m)[2:].rstrip("L").rjust(halflen, "0")
    # bm = map(int, bm)
    
    # print(bin(m),)
    # arr = []
    # arr2 = []
    # for i in range(1, halflen + 1):
    #     if bm[i - 1]:
    #         arr.append(i + 1)
    #         arr2.append(i)
    #     else:
    #         arr.append(i)
    #         arr2.append(i + 1)
    # if n & 1:
    #     arr.append(n)
    # arr += arr2
    
    print(" ").join(str(x) for x in arr)