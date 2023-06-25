    n, m, k, x, y = map(int, input().split())
    
def cnt(r, c):
        a = k
        if n == 1:
            return (a // m + ((a % m) >= c))
        res = a // ((2 * n - 2) * m)
        if r != 1 and r != n:
            res *= 2
        a %= (2 * n - 2) * m
        if a > n * m:
            return res + 1 + (1 if r != n and a-n*m >= (n-r-1)*m + c else 0)
        else:
            return res + (1 if a >= (r-1)*m + c else 0)
    
    r1 = cnt(1, 1)
    r2 = cnt(2, 1)
    r3 = cnt(n - 1, 1)
    r4 = cnt(n, m)
    r5 = cnt(x, y)
    print(max(r1, r2, r3), r4, r5)