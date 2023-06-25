    import sys
    from array import array
    
    input = lambda: sys.stdin.buffer.readline().decode().strip()
    inp = lambda dtype: [dtype(x) for x in input().split()]
    inp_2d = lambda dtype, n: [dtype(input()) for _ in range(n)]
    inp_2ds = lambda dtype, n: [inp(dtype) for _ in range(n)]
    ceil1 = lambda a, b: (a + b - 1) // b
    debug = lambda *x: print(*x, file=sys.stderr)
    
    
def fact(be, en):
        res, res2 = [1] * (en + 1), [1] * (en + 1)
        for i in range(be, en + 1):
            res[i] = mult(res[i - 1], i)
            res2[i] = inv(res[i])
        return res, res2
    
    
def ncr(n, r):
        if n < r:
            return 0
        return mult(mult(facs[n], invs[n - r]), invs[r])
    
    
    mod = 10 ** 9 + 7
    add = lambda a, b: (a % mod + b % mod) % mod
    mult = lambda a, b: (a % mod * b % mod) % mod
    inv = lambda a: pow(a, mod - 2, mod)
    
    n, k = inp(int)
    facs, invs = fact(1, n)
    k, ans = min(k, n), 1
    
    for i in range(1, k + 1):
        ans += ncr(n, i)
    print(ans % mod)