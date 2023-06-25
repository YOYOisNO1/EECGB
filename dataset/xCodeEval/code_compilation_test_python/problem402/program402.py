def program402():
    from itertools import *
    from fractions import *
    import sys
    a, b, c = sorted (map (lambda x: x[2] if x[1] == '>' else x[0], [input () for _ in range (3)]))
    x = {a, b, c}
    print 'Impossible'  if x >= {'A', 'B', 'C'} else b + list (x - {b})[0] + list ({'A', 'B', 'C'} - x)[0]
       