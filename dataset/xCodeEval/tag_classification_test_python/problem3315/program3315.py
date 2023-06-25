def program3315():
    import sys, math
    from sys import stdin, stdout
    
    rem = 10 ** 9 + 7
    inf = 10 ** 18
    sys.setrecursionlimit(10 ** 6 + 7)
    # from resource import *; setrlimit(RLIMIT_STACK, (RLIM_INFINITY, RLIM_INFINITY))
    take = lambda: map(int, stdin.readline().split())
    from heapq import heappush, heappop, heapify
    from collections import deque
    from bisect import *
    
    n,m,r=take()
    a=min(take())
    b=max(take())
    ans=r
    x=r/a
    req=r%a
    ans=max(ans,x*b+req)
    print(ans)
    