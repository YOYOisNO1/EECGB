    from fractions import gcd
    
    
def get_divisors(n):
        divs = []
        i = 1
        while i <= n / i:
            if n % i == 0:
                divs.append(i)
                if n / i != i:
                    divs.append(n / i)
            i += 1
        return divs
    
    
def f(x, y):
        divs = get_divisors(x)
        dd = {}
        for d in divs:
            mul = y/d*d
            if not mul:
                continue
            if mul not in dd or dd[mul] < d:
                dd[mul] = d
        dd = sorted(dd.items(), reverse=True)
        dd.append((0, 0))
        # for k, w in dd:
        #    print k, w
        ans = 0
        ix = 0
        while y and ix < len(dd):
            y, g = dd[ix]
            # print y, g, ix
            next_y, next_ix = None, None
            for i in xrange(ix+1, len(dd)):
                # print i, dd[i], dd[i][1] % g
                if dd[i][1] % g == 0:
                    next_y = dd[i][0]
                    next_ix = i
                    break
            ans += (y-next_y) / g
            ix = next_ix
            y -= (y-next_y) / g * g
        return ans
    
    
def brute(x, y):
        ans = 0
        while y:
            ans += 1
            # print 'x=%d, y=%d->%d, gcd=%d, ans=%d' % (x, y, y-gcd(x, y),
            #                                          gcd(x, y), ans)
            y = y - gcd(x, y)
        return ans
        # if not y:
        #     return 0
        # return 1+brute(x, y-gcd(x, y))
    
    
    a, b = map(int, input().split())
    print f(a, b)
    # print brute(2*2*3*5, 2*3*3+1)
    # print brute(2*3*3, 2*2*3*5)
    # print brute(2*3, 59)
    # print brute(59, 6)
    
    # assert brute(6, 3) == 1
    # assert brute(3, 5) == 3
    # for i in xrange(1, 100):
    #     for j in xrange(1, 100):
    #        assert brute(i, j) == f(i, j)
    # assert f(10**9+9, 10**9+8) == 10**9+8