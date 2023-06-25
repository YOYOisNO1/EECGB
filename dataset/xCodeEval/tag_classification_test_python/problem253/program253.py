    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
    import sys
    input = sys.stdin
    output = sys.stdout
    
    Vv = ['A', 'E', 'I', 'O', 'U', 'Y']
    Vv.extend([v.lower() for v in Vv])
    V = set(Vv)
    
def solve(S):
        S = S[:-1]
        S = S.strip()
        if S[-1] in V:
            return 'YES'
        else:
            return 'NO'
    
    S = input.readline().strip()
    
    a = solve(S)
    output.write('%s\n' % a)