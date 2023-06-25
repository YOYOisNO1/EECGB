def program7562():
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
    if not d: print("Marsel")
    else:
        print(["Timur",) "Marsel"][1 - (n & 1)]
    