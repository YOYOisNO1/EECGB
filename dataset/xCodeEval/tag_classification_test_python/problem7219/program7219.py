    # -*- coding: utf-8 -*-
    from collections import deque
    
def calc(n, m):
        if n == 1:
            return [[1, 0], [0, 1]]
        a = calc(n // 2, m)
        if n % 2 == 0:
            res00 = (a[0][0] * a[0][0]) % m
            res00 = (res00 + a[0][0] * a[1][0]) % m
            res00 = (res00 + a[0][1] * a[0][0]) % m
            res01 = (a[0][0] * a[0][1]) % m
            res01 = (res01 + a[0][0] * a[1][1]) % m
            res01 = (res01 + a[0][1] * a[0][1]) % m
            res10 = (a[1][0] * a[0][0]) % m
            res10 = (res10 + a[1][0] * a[1][0]) % m
            res10 = (res10 + a[1][1] * a[0][0]) % m
            res11 = (a[1][0] * a[0][1]) % m
            res11 = (res11 + a[1][0] * a[1][1]) % m
            res11 = (res11 + a[1][1] * a[0][1]) % m
            return [[res00, res01], [res10, res11]]
        else:
            res00 = (a[0][0] * a[0][0] * 2) % m
            res00 = (res00 + a[0][0] * a[1][0]) % m
            res00 = (res00 + a[0][1] * a[0][0]) % m
            res00 = (res00 + a[0][1] * a[1][0]) % m
            res01 = (a[0][0] * a[0][1] * 2) % m
            res01 = (res01 + a[0][0] * a[1][1]) % m
            res01 = (res01 + a[0][1] * a[0][1]) % m
            res01 = (res01 + a[0][1] * a[1][1]) % m
            res10 = (a[1][0] * a[0][0] * 2) % m
            res10 = (res10 + a[1][0] * a[1][0]) % m
            res10 = (res10 + a[1][1] * a[0][0]) % m
            res10 = (res10 + a[1][1] * a[1][0]) % m
            res11 = (a[1][0] * a[0][1] * 2) % m
            res11 = (res11 + a[1][0] * a[1][1]) % m
            res11 = (res11 + a[1][1] * a[0][1]) % m
            res11 = (res11 + a[1][1] * a[1][1]) % m
            return [[res00, res01], [res10, res11]]
    
def binpow(a, p, m):
        if p == 0:
            return 1 % m
        if p == 1:
            return a % m
        ans = binpow(a, p // 2, m)
        ans = (ans * ans) % m
        if p % 2 == 1:
            ans = (ans * a) % m
        return ans
    
    n, k, l, m = map(int, input().split())
    ans = [0, 0]
    x = calc(n, m)
    ans[0] = (x[0][0] + x[0][1] + x[1][0] + x[1][1]) % m
    ans[1] = ((binpow(2, n, m) - ans[0]) % m + m) % m
    res = 1
    
    for i in range(l):
        res = (res * ans[k & 1]) % m
        k >>= 1  
    
    if k > 0:
        res = 0
    
    print(res % m)