def program2379():
    q, w = map(int, input().split())
    e = [1] * (q)
    r = [1] * (q)
    z = 0
    w -= 1
    while sum(r) > 0:
        if e[w] == 0 and r[w] == 1:
            r[w] = 0
        elif r[w] == 0:
            if (q - w > w or 1 not in r[w:])and 1 in r[:w]:
                w -= 1
            else:
                w += 1
        else:
            if 0 in r:
                e[r.index(0)] += 1
                e[w] -= 1
            else:
                if w >= q - 1:
                    e[w - 1] += 1
                else:
                    e[w + 1] += 1
                e[w] -= 1
        z += 1
    print(z)