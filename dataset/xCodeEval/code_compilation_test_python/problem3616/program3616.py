    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    n, m = [int (i) for i in input ().split ()]
    
def brute ():
        p = []
        for i in range (1, n + 1):
            for j in range (1, n + 1):
                if (i * i + j * j) % m == 0:
                    p.append ((i, j))
        return p
    
    
    ret = 0
    if m == 1:
        print n * n
    else:
        print len (brute ())
    