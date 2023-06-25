def program6122():
    from math import *
    
    s = []
    cpt = 0
    r1, c1, r2, c2 = map(int, input().split())
    if r1 == r2:
        s += [1]
        if (c2 - c1) % 2 != 0:
            s += [0]
        else:
            s += [2]
        s += [abs(c1 - c2)]
    elif r1 != r2:
        cpt=(abs(r1 - r2) + abs(c2 - c1))
        if c1 == c2:
            s += [1]
        else:
            s +=[2]
        if abs(r1 - r2) == abs(c1 - c2):
            s += [1]
    
        elif cpt % 2 != 0:
            s += [0]
        else:
            s += [2]
        if abs(r1 - r2) == abs(c1 - c2):
            s += [abs(r1 - r2)]
        else:
            if abs(r1 - r2) < abs(c1 - c2):
                s += [abs(abs(c1 - c2))]
            else:
                s += [abs(abs(r1 - r2))]
    
    print(*s)