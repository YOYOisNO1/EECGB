    from itertools import *
    
    l1, r1, l2, r2 = map(int, input().split())
    la = []
    lb = []
    
def foo(l, r, pv, li):
        if l > r or pv < 1:
            return
        while r < pv:
            pv /= 2
        while l > pv:
            l -= pv
            r -= pv
        li.append((l, r))
        if l < r:
            foo(l, pv - 1, pv / 2, li)
            foo(pv + 1, r, pv / 2, li)
    
    pv = 2 ** 32
    foo(l1, r1, pv, la)
    foo(l2, r2, pv, lb)
    
    ans = 0
    #print la
    #print lb
    for a in la:
        for b in lb:
            if a == b:
                ans = max(ans, a[1] - a[0] + 1)
            else:
                ans = max(ans, min(a[1], b[1] - max(a[0], b[0])))
    print ans