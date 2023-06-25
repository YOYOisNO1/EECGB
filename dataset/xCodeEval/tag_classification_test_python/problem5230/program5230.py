    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
    import sys
    input = sys.stdin
    output = sys.stdout
    
    M = ['S','H','D','C']
    V = ['6','7','8','9','T','J','Q','K','A']
    
def solve(km,c1,c2):
        v = lambda c: V.index(c[0])
        m = lambda c: M.index(c[1])
        m1 = m(c1)
        m2 = m(c2)
        v1 = v(c1)
        v2 = v(c2)
        if m1 == m2:
            if v1 > v2:
                return 'YES'
        else:
            if m1 == M.index(km):
                return 'YES'
        return 'NO'
    
    km = input.readline().strip()
    C = input.readline().strip().split(' ')
    c1 = C[0]
    c2 = C[1]
    
    a = solve(km,c1,c2)
    output.write('%s\n' % a)