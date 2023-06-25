def program4440():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    s = input ()
    s = s.replace ("dot", ".")
    if s [0] == '.': s = "dot" + s [1:]
    if s [-1] == '.': s = s [:-1] + "dot"
    idx = s [1:].find ("at")
    s = s [:idx + 1] + "@" + s [idx + 3:]
    print(s)