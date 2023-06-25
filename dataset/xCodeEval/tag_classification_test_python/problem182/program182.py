def program182():
    k = int(input())
    d = {'.': 0}
    for _ in range(4):
        for c in input():
            if c == '.': continue
            d[c] = d.get(c, 0) + 0.5
    print("NO" if max(d.values()) > k else "YES")