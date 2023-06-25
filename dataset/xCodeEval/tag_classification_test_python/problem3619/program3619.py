def program3619():
    import sys
    import copy
    R = lambda:map(int,input().split())
    n,t = R()
    s = input()
    if n is 1: print(s)
    else:
        row = []
        for i in xrange(n):
            if s[i] is "B": row.append(1)
            else: row.append(0)
    
        for j in xrange(t):
            poyo = []
            for i in xrange(n):
                if row[n-1-i] is 0:
                    if i is n-1:
                        poyo.insert(0, 0)
                    elif row[n-2-i] is 1:
                        poyo.insert(0, 1)
                    else:
                        poyo.insert(0, 0)
                else:
                    if i is 0:
                        poyo.insert(0, 1)
                    elif row[n-i] is 1:
                        poyo.insert(0, 1)
                    else:
                        poyo.insert(0, 0)
            row = copy.deepcopy(poyo)
    
        agepoyo = []
        for i in xrange(n):
            if row[i] is 1:
                agepoyo.append("B")
            else:
                agepoyo.append("G")
        print("").join(agepoyo)