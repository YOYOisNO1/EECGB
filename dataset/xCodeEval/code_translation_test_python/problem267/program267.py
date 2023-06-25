def program267():
    #!/usr/bin/env python
    #-*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    s = input ()
    ret, start = 0, 0
    for i in s:
        x = ord (i) - ord ('a')
        y = min ((start - x) % 26, (x - start) % 26)
        ret += y
        start = x
    print(ret)
    