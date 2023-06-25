def program7816():
    s = input()
    n = int(input())
    
    t = [j for j, q in enumerate(s) if q == 'T']
    l, r = [0] * 101, [0] * 101
    
    for i, (a, b) in enumerate(zip([-1] + t, t + [len(s)])):
        v = b - a
        u = v - 1
    
        for k in range(i, 0, -1):
            l[k] = max(l[k] + u, l[k - 1] + v)
            r[k] = max(r[k] - u, r[k - 1] - v)
            u, v = -u, -v
    
        r[i + 1] = l[i] - 1
    
        l[0] += u
        r[0] -= u
    
    print(max(l[n % 2:n + 1:2] + r[n % 2:n + 1:2]))