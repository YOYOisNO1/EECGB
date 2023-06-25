def program7103():
    p, k = map(int, input().split())
    if k == 0:
        print(pow(p,) p - 1, 1000000007)
    elif k == 1:
        print(pow(p,) p, 1000000007)
    else:
        x = 1
        for i in xrange(1, p + 1):
            x = x * k % p
            if x == 1:
                break
        print(pow(p,) (p - 1) / i, 1000000007)