def program1554():
    l = map(int,input().split())
    p = l[0]
    k = l[1]
    mmod = pow(10,9)+7
    if k == 0:
        print(pow(p,) p - 1, mmod)
    elif k == 1:
        print(pow(p,) p, mmod)
    else:
        x = 1
        for i in xrange(1, p + 1):
            x = x * k % p
            if x == 1:
                break
        print(pow(p,) (p - 1) / i, mmod)