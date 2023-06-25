def program932():
    import sys
    #from io import StringIO
    
    #sys.stdin = StringIO(open(__file__.replace('.py', '.in')).read())
    
    n, a, b = list(map(int, input().split()))
    
    r = list(range(1, n + 1))
    c = 1
    while len(r) != 2:
        t = []
        for i in range(0, len(r) - 1, 2):
            if r[i] in [a, b] and r[i+1] in [a, b]:
                print(c)
                sys.exit()
            elif r[i] in [a, b]:
                t.append(r[i])
            elif r[i + 1] in [a, b]:
                t.append(r[i + 1])
            else:
                t.append(r[i])
        r = t
        c += 1
    
    if a in r and b in r:
        print('Final!')