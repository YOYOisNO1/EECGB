def program5893():
    import sys, math
    n, c = int(input()), list(map(int, input().split()))
    n += 1
    c.insert(0, 0)
    done, t = [False] * n, []
    for i in range(1, n):
        a, ct = i, 0
        while not done[a]:
            done[a] = True
            ct, a = ct + 1, c[a]
        if a is not i:
            print(-1)
            sys.exit(0)
        if ct > 0:
            if ct & 1 is 0:
                ct //= 2
            t.append(int(ct))
    m = t[0]
    for i in range(1, len(t)):
        g = math.gcd(m, t[i])
        m = m * t[i] // g
    print(m)