    """
        Template written to be used by Python Programmers.
        Use at your own risk!!!!
        Owned by adi0311(rating - 5 star at CodeChef and Specialist at Codeforces).
    """
    import sys
    import heapq
    from math import *
    from collections import defaultdict as dd  # defaultdict(<datatype>) Free of KeyError.
    from collections import deque  # deque(list) append(), appendleft(), pop(), popleft() - O(1)
    from collections import Counter as c  # Counter(list)  return a dict with {key: count}
    from itertools import combinations as comb
    from bisect import bisect_left as bl, bisect_right as br, bisect
    # sys.setrecursionlimit(2*pow(10, 6))
    # sys.stdin = open("input.txt", "r")
    # sys.stdout = open("output.txt", "w")
    mod = pow(10, 9) + 7
    mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(var): sys.stdout.write(var)
def l(): return list(map(int, data().split()))
def sl(): return list(map(str, data().split()))
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [[val for i in range(n)] for j in range(m)]
    
    
def first():
        global a, b, e, d
        div, mul = e, a
        a1, a2 = e*mul, a*mul
        if a2 / div > b:
            return mod, 1
        return a*b*e-d*a*a, div
    
    
def second():
        global a, b, e, d
        div, mul = d, b
        a1, a2 = e * mul, d * mul
        if a1 / div > a:
            return mod, 1
        return d*a*b-e*b*b, div
    
    
    a, b, e, d = sp()
    t1 = first()
    t2 = second()
    if t1[0]/t1[1] < t2[0]/t2[1]:
        diff, area = t1[0], a * b * t1[1]
    else:
        diff, area = t2[0], a * b * t2[1]
    g = gcd(diff, area)
    out(str(diff//g)+"/"+str(area//g))