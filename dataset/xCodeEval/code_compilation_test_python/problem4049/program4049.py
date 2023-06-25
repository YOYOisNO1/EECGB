    import os
    from io import BytesIO
    from math import trunc
    
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    fmod = lambda x: x - 998244353.0 * trunc(x / 998244353.0)
    mod_prod = lambda a, b: fmod(trunc(a / 65536.0) * fmod(b * 65536.0) + (a - 65536.0 * trunc(a / 65536.0)) * b)
    
    
def fpow(x, y):
        res = 1.0
        while y > 0:
            if y & 1 == 1:
                res = mod_prod(res, x)
            x = mod_prod(x, x)
            y >>= 1
    
        return res
    
    
def ntt(a, inv=False):
        n = len(a)
        w = [1.0] * (n >> 1)
    
        w[1] = fpow(3.0, 998244352 / n)
        if inv:
            w[1] = fpow(w[1], 998244351)
    
        for i in xrange(2, (n >> 1)):
            w[i] = mod_prod(w[i - 1], w[1])
    
        rev = [0] * n
        for i in xrange(n):
            rev[i] = rev[i >> 1] >> 1
            if i & 1 == 1:
                rev[i] |= (n >> 1)
            if i < rev[i]:
                a[i], a[rev[i]] = a[rev[i]], a[i]
    
        step = 2
        while step <= n:
            half, diff = step >> 1, n / step
            for i in xrange(0, n, step):
                pw = 0
                for j in xrange(i, i + half):
                    v = mod_prod(a[j + half], w[pw])
                    a[j + half] = a[j] - v
                    a[j] += v
                    pw += diff
    
            step <<= 1
    
        if inv:
            inv_n = fpow(n, 998244351)
            for i in xrange(n):
                a[i] = mod_prod(a[i], inv_n)
    
    
def conv(a, b):
        s = len(a) + len(b) - 1
        n = 1 << s.bit_length()
    
        a.extend([0.0] * (n - len(a)))
        b.extend([0.0] * (n - len(b)))
    
        ntt(a)
        ntt(b)
    
        for i in xrange(n):
            a[i] = mod_prod(a[i], b[i])
    
        ntt(a, inv=True)
        del a[s:]
    
    
def main():
        N, _ = input().split()
        n = int(N) >> 2
    
        d = [0.0] * 10
        for i in input().split():
            d[int(i)] = 1.0
    
        result = [1.0]
        while n > 0:
            if n & 1 == 1:
                conv(result, d[:])
            conv(d, d[:])
            n >>= 1
    
        os.write(1, str(int(sum(mod_prod(i, i) for i in result) % 998244353.0)))
    
    
    if __name__ == '__main__':
        main()