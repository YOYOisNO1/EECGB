def program4484():
    #510_A
    
    n = int(input())
    p = int(input())
    
    ms = []
    for i in range(0, n):
        m = int(input())
        ms.append(m)
    
    mx = max(ms)
    m2 = mx + p
    diffs = sum([mx - i for i in ms])
    
    if p < diffs:
        m1 = mx
    else:
        m1 = (p - diffs)
        if m1 % n != 0:
            m1 = m1 // n + 1
        else:
            m1 = m1 // n
        m1 += mx
    
    print(m1, m2)