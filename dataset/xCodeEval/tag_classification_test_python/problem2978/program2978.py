def program2978():
    #!/usr/bin/env python
    #-*- coding: utf-8 -*-
    
    from collections import defaultdict
    from math import factorial as f
    from fractions import gcd as g
    
    l = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
    s = input ()
    print(["NO",) "YES"][sum (s.count (i) for i in l) == 1]
    