def func(n, m, l, r):
        hm = m // 2
        hn = n // 2
        ans = 0
        if l <= hm:
            ans += func(hn, hm, l, min(hm,r))
        if l <= hm + 1 and hm + 1 <= r:
            ans += n % 2
        if r >= hm + 2:
            ans += func(hn, hm, max(l,hm+2)-hm-1, r-hm-1)
        return ans
    
    n, l, r = map(int, input().split())
    d = len('{0:b}'.format(n))
    m = 2**d - 1
    print(func(n,) m, l, r)