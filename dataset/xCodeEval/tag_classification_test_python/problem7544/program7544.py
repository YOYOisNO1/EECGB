def program7544():
    #!/usr/bin/env python
    #-*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    n, m, k = [int (i) for i in input ().split ()]
    lim = int (m ** 0.5)
    d = []
    for i in range (1, lim + 1):
        if m % i == 0:
            if i >= k and i < m:
                d.append (i)
            if m != m / i:
                if (m / i) >= k and (m / i) < m:
                    d.append (m / i)
    # print(d)
    if not d: print("Marsel")
    else:
        a = len (d) & 1
        b = n & 1
        # print(a,) b
        # 0 0 m
        # 1 1 t
        # 1 0 m
        # 0 1 t
        print(["Timur",) "Marsel"][1 - b]
    