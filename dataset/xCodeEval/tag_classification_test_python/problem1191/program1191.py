def program1191():
    l, r, a = [int(x) for x in input().split()]
    if l > r:
        o = l - r
        if o > a:
            print((r + a) * 2)
        else:
            print(2 * (l + (a - o) // 2))
    else:
        o = r - l
        if o > a:
            print((l + a) * 2)
        else:
            print(2 * (r + (a - o) // 2))