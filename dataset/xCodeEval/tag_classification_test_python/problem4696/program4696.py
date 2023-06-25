def program4696():
    from random import random
    import math
    import re
    import fractions
    
    # N = input()
    N, K = map(int, input().split(" "))
    S = input()
    seq = []
    for i in xrange(26):
        c = chr(ord("A")+i)
        if c in S:
            s = S.index(c)
            e = S.rindex(c)
            seq.append((s, -1, c))
            seq.append((e, 1, c))
    seq.sort()
    mx = 0
    for g in seq:
        mx -= g[1]
        # print(mx,) g
        if mx > K:
            print("YES")
            break
    else:
        print("NO")