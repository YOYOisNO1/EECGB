def program2681():
    from sys import stdin
    
    a, b, c, d, e, f = map(int, stdin.read().split())
    res = [3]
    for _ in 0, 1:
        if a == c == e:
            res.append(1)
        for _ in range(3):
            if a == c and not (b < f < d or b > f > d):
                res.append(2)
            a, b, c, d, e, f = c, d, e, f, a, b
        a, b, c, d, e, f = b, a, d, c, f, e
    print(min(res))