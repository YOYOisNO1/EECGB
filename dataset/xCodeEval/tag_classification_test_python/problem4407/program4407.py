def program4407():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    s = input ()
    t = s [1:-1].replace ("at", "@", 1).replace ("dot", ".")
    print(s) [0] + t + s [-1]