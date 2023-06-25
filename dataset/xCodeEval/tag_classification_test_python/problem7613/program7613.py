    import os, sys
    from math import trunc
    
    MOD = 998244353
    MODF = float(MOD)
    SHRT = float(1 << 16)
    G = 3.0
    MAXSIZ = 1 << 20
    
    # Using pajenegod's crazy method for multiplication using floating point
    fmod = lambda x: x - MODF * trunc(x / MODF)
    mod_prod = lambda a, b: fmod(trunc(a / SHRT) * fmod(b * SHRT) + (a - SHRT * trunc(a / SHRT)) * b)
def fpow(a, b):
        r = 1.0
        while b:
            if b & 1: r = mod_prod(r, a)
            if b > 1: a = mod_prod(a, a)
            b >>= 1
        return r
    
    inp = os.read(sys.stdin.fileno(), 10 ** 8).split()
    n, k = int(inp[0]), int(inp[1])
    f = [0.0] * MAXSIZ
    for i in xrange(2, k + 2):
        f[int(inp[i])] = 1.0
    
    m = MAXSIZ
    m2 = m / 2
    w = [1.0] * m2
    w[1] = fpow(G, (MOD - 1) / m)
    for i in xrange(2, m2):
        w[i] = mod_prod(w[i - 1], w[1])
    
    rev = [0] * m
    for i in xrange(m):
        rev[i] = rev[i >> 1] >> 1
        if i & 1: rev[i] |= m2
    
def ntt_transform(a):
        for i in xrange(m):
            if i < rev[i]: a[i], a[rev[i]] = a[rev[i]], a[i]
        l = 2
        while l <= m:
            half, diff = l >> 1, m / l
            for i in xrange(0, m, l):
                pw = 0
                for j in xrange(i, i + half):
                    v = mod_prod(a[j + half], w[pw])
                    a[j + half] = a[j] - v
                    a[j] = a[j] + v
                    pw += diff
            l <<= 1
    
    
    ntt_transform(f)
    f = [fpow(x, n >> 1) for x in f]
    ntt_transform(f)
    
    inv_m = fpow(m, MOD - 2)
    ans = mod_prod(sum(mod_prod(x, x) for x in f) % MODF, mod_prod(inv_m, inv_m))
    os.write(sys.stdout.fileno(), str(int(ans)))