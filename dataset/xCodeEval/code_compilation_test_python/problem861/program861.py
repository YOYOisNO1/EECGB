def program861():
    import math
    
    n = int(input())
    s = input()
    a = []
    p = []
    t = 0
    f = 1
    
    for i in range(n):
        a.append(int(s[i]))
        t += a[i]
        p.append(t)
    
    for i in range(n):
        s = p[i]
        f = 1
        t = 0
        k = i+1
        c = 0
        for j in a[k:n]:
            t += j
            if c and !t: continue
            if j == n-1 and t != s:
                f = 0
            elif t == s:
                t = 0
                c += 1
            elif t > s:
                f = 0
                break
        if i == n-1 and f: f = 0
        if f: break
    
    if f: print('YES')
    else: print('NO')