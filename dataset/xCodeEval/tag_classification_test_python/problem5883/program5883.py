def program5883():
    import sys, math
    n, c = int(input()), list(map(int, input().split()))
    n += 1
    c.insert(0, 0)
    done, t = [False] * n, []
    for i in range(1, n):
        a = i
        ct = 0
        while not done[a]:
            ct += 1
            done[a] = True
            a = c[a]
        if a is not i:
            print(-1)
            sys.exit(0)
        if ct > 0:
            if ct & 1 is 0:
                ct /= 2
            t.append(int(ct))
            #print(i, ct)
    g, m = t[0], t[0]
    for i in range(1, len(t)):
        g = math.gcd(m, t[i])
        m = m * t[i] // g
        #print(g, m)
    print(m)
    