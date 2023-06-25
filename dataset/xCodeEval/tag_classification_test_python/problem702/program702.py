def program702():
    #!/usr/bin/env python
    #-*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    a, b, x, y = [int (i) for i in input ().split ()]
    f = g (x, y)
    x, y = x / f, y / f
    lo, hi, ret = 1, max (a, b), 0
    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if (mid * x <= a) and (mid * y) <= b:
            ret = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ret) * x, ret * y
    