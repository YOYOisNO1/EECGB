    """
        Template written to be used by Python Programmers.
        Use at your own risk!!!!
        Owned by adi0311(rating - 5 star at CodeChef and Specialist at Codeforces).
    """
    import sys
    from functools import lru_cache, cmp_to_key
    from heapq import merge, heapify, heappop, heappush, nlargest, nsmallest, _heapify_max, _heapreplace_max
    from math import ceil, floor, gcd, fabs, factorial, fmod, sqrt, inf, log
    from collections import defaultdict as dd, deque, Counter as c
    from itertools import combinations as comb, permutations as perm
    from bisect import bisect_left as bl, bisect_right as br, bisect
    from fractions import Fraction
    # sys.setrecursionlimit(2*pow(10, 6))
    # sys.stdin = open("input.txt", "r")
    # sys.stdout = open("output.txt", "w")
    mod = pow(10, 9) + 7
    mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(var): sys.stdout.write(str(var))
def outln(var): sys.stdout.write(str(var)+"\n")
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
    
    
def dfs(source, p):
        global cycle_number
        if color[source] == 2:
            return
        if color[source] == 1:
            cycle_number += 1
            cur = p
            mark[cur] = cycle_number
            while cur != source:
                cur = par[cur]
                mark[cur] = cycle_number
            return
        par[source] = p
        color[source] = 1
        for child in graph[source]:
            if child == par[source]:
                continue
            dfs(child, source)
        color[source] = 2
    
    
    n = int(data())
    graph = dd(set)
    color, par, mark = [0] * (n+1), [0] * (n+1), [0] * (n+1)
    cycles = [[]] * (n+1)
    cycle_number = 0
    for i in range(n):
        u, v = sp()
        graph[u].add(v)
        graph[v].add(u)
    cnt = 0
    for i in range(1, 6):
        if len(graph[i]) <= 1:
            cnt += 1
    if cnt >= 3:
        outln("WIN")
        exit()
    dfs(1, 0)
    for i in range(1, n + 1):
        if mark[i] != 0:
            cycles[mark[i]].append(i)
    for i in cycles:
        if len(i) == 3:
            outln("WIN")
            exit()
    outln("FAIL")