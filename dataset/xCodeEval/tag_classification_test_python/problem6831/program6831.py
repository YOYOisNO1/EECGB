def f():
        k, t = int(input()), input()
        j, n = 0, (len(t) + 1) // 2
        p = [0] * n
    
        q = 'abcdefghijklmnopqrstuvwxyz'[: k]
        r = {x: 0 for x in q}
        r['?'] = 0
    
        for i in range(n):
            x, y = t[i], t[- 1 - i]
            if x == '?': x = y
            elif y != '?' and x != y: return 'IMPOSSIBLE'
            if not x in r: return 'IMPOSSIBLE'
            r[x] += 1
            p[i] = x
    
        y = ''.join(x for x in q if not r[x])
        if len(y) > r['?']: return 'IMPOSSIBLE'
        y = 'a' * (r['?'] - len(y)) + y
        
        for i in range(n):
            if p[i] == '?':
                p[i] = y[j]
                j += 1
        p += reversed(p[: len(t) // 2])
        return ''.join(p)
    
    print(f())