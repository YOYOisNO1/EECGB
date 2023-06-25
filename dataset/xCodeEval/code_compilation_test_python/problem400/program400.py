def program400():
    from itertools import *
    from fractions import *
    import sys
    a, b, c = sorted (map (lambda x: x[2] if x[1] == '>' else x[0], [input () for _ in range (3)]))
    print 'Impossible'  if len ({a, b, c}) == 3 else b + list ({a, b, c} - {b})[0] + list ({'A', 'B', 'C'} - {a, b, c})[0]
       