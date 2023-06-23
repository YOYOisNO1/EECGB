    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    from heapq import heappush,heappop,heapify
    import math
    from collections import *
    from functools import reduce,cmp_to_key,lru_cache
    import sys
    input = sys.stdin.readline
    M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
     
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]
    
    l1 = k = n = 0
    l = []
    
def givedepth(d, time):
        global k
        time %= 2 * k
        if time <= k:return d + time
        return d + 2 * k - time
    
    
    
    for _ in range(val()):
        n, k, l1 = li()
        l = li()
        # print(l , k, l1)
    
    
    
        # @lru_cache(None)
    def rec(i, time):
            global n, l, l1
            # print(i, time)
            if i == n + 1:
                rec.ans = 1
                return 0
            if givedepth(l[i - 1], time) > l1:return 0
            for j in range(2 * k):
                rec(i + 1, (time + 1 + j) % (2 * k))
                if givedepth(l[i - 1], time + 1 + j) > l1:return 0
            return 0
    
        rec.ans = 0
        for i in range(2 * k):
            rec(1, i)
        print('YES' if rec.ans else 'NO')