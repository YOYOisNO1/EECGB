def program485():
    s = input()
    r = 0
    h = int(s)
    while 1:
        l = list(s)
        d = list(map(int, s))
        n = ''.join(l)
        m = int(n)
        f = max(d)
        m = m-f
        s = str(m)
        r += 1
        if m<=0:
            break
    print(0 if h == 0 else r)