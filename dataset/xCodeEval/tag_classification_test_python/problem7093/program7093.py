def fpow(b, e, mod):
        ans = 1
        while e:
            if e & 1:
                ans = (ans * b) % mod
            b = b**2 % mod
            e >>= 1
        return ans
    
    p, k = map(int, input().split())
    mod = 10**9 + 7
    
    if k == 0:
        print(fpow(p, p - 1, mod))
    elif k == 1:
        print(fpow(p, p, mod))
    else:
        ans = lim = p - 1
        d = 1
        while d*d <= lim:
            if lim % d == 0:
                if fpow(k, d, p) == 1:
                    ans = d
                    break
                aux = lim / d
                if aux != d and fpow(k, aux, p) == 1:
                    ans = lim = aux
                    d = 1
            d += 1
        print(fpow(p, (p - 1) / ans, mod))