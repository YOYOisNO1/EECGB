def program2434():
    n, = map(int, input().split(" "))
    st = input()
    isin = 0
    a = [0,0]
    t = 0
    for ch in st:
        if ch in ('(',')'):
            if isin == 0:
                a[isin] = max(a[isin], t)
            elif t:
                a[isin] += 1
            t = 0
            if ch == ')':
                isin = 0
            else:
                isin = 1
        elif ch == '_':
            if isin:
                if t:
                    a[isin] += 1
            else:
                a[isin] = max(a[isin], t)
            t = 0
        else:
            t += 1
    a[isin] = max(a[isin], t)
    print(a[0],) a[1]