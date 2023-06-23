    import sys,os,math
    from collections import Counter, defaultdict
    import bisect
    from sys import stdin, stdout
    from itertools import repeat, izip
    
    
    # n, k = map(int, input().split())
    # da = map(int, input().split())
    # db = map(int, input().split())
    
    
    n, m = map(int, input().split())
    da = map(int, input().split())
    di = defaultdict(list)
    total = sum(da)
    for i in xrange(m):
        a, b = map(int, input().split())
        di[b].append(a)
    for k in di:
        di[k].sort()
    l, r = 0, 2*total
    while l<r:
    def ck(day):
            p = []
            for k in di:
                idx = bisect.bisect(di[k], day)
                if idx != 0:
                    p.append((di[k][idx-1], k))
            tt = total
            cost = 0
            p.sort()
            for ld, k in p:
                by = min(da[k-1], ld-cost)
                cost += by
                tt -= by
            if day-cost>= tt*2:
                return 1
            else:
                return 0
        mid = (l+r)/2
        if ck(mid):
            r = mid
        else:
            l = mid + 1
    print l