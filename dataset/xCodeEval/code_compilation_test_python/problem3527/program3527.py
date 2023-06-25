def f(q, t):
        a, b, c = sorted(q)
        if t == '**': return a * b * c
        if t == '++': return a + b + c
        if t == '*+': return a * b + c
        if t == '+*': return a * (b + c)
    
    p = sorted(list(map(int, input().split())))
    t = input()[:: 2]
    x, t = t[0], t[1: ]
    if x == '*':
        s = p[0] * p[1] * p[2] * p[3]
        for i in range(3):
            for j in range(i + 1, 4):
                q = p[:]
                q[i] *= q[j]
                q.pop(j)
                s = min(f(q, t), s)
        print(s)
    else: print(f([p[0], p[1], p[2] + p[3]]))