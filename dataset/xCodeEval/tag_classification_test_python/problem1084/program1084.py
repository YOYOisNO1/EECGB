    import sys, math
    import io, os
    #data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    from bisect import bisect_left as bl, bisect_right as br, insort
    from heapq import heapify, heappush, heappop
    from collections import defaultdict as dd, deque, Counter
    # from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
    from decimal import Decimal
    # from fractions import Fraction
    # sys.setrecursionlimit(100000)
    mod = 998244353
    INF=float('inf')
    
def cal(p,q,i):
        if i==2:
            p1 = p[::]
            q1 = q[::]
            p1[i] = max(p1[i] - q1[i - 1], 0)
            q1[i - 1] = max(q1[i - 1] - p1[i], 0)
            p1[i] = max(p1[i] - q1[i], 0)
            q1[i] = max(q1[i] - p1[i], 0)
            p[i] = max(p[i] - q[i], 0)
            q[i] = max(q[i] - p[i], 0)
            p[i] = max(p[i] - q[i - 1], 0)
            q[i - 1] = max(q[i - 1] - p[i], 0)
            return min(sum(p1),sum(p))
        p1=p[::]
        q1=q[::]
        p1[i] = max(p1[i] - q1[i - 1], 0)
        q1[i - 1] = max(q1[i - 1] - p1[i], 0)
        p1[i] = max(p1[i] - q1[i], 0)
        q1[i] = max(q1[i] - p1[i], 0)
        ans=cal(p1,q1,i+1)
        p[i] = max(p[i] - q[i], 0)
        q[i] = max(q[i] - p[i], 0)
        p[i] = max(p[i] - q[i - 1], 0)
        q[i - 1] = max(q[i - 1] - p[i], 0)
        return min(ans,cal(p, q, i + 1))
    
    n=int(data())
    a=mdata()
    b=mdata()
    p=a[::]
    q=b[::]
    s=0
    for i in range(3):
        s+=min(a[i],b[(i+1)%3])
    print(cal(p,q,0),s)
    