def program430():
    h, n = map(int, input().split())
    s, k = 0, 1 << h - 1
    while k:
        if n > k:
            s += 1 if s & 1 else k << 1
            n -= k
        else: s += k << 1 if s & 1 else 1
        k >>= 1
    print(s)