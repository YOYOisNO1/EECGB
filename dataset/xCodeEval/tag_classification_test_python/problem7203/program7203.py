    # -*- coding: utf-8 -*-
    from collections import deque
    
def calc(n, m):
        if n == 1:
            return [[1, 0], [0, 1]]
        a = calc(n // 2, m)
        res = [[0, 0], [0, 0]]
    
        if n % 2 == 0:
            for i in range(2):
                for j in range(2):
                    res[i][j] = (res[i][j] + a[i][0] * a[0][j]) % m
                    res[i][j] = (res[i][j] + a[i][0] * a[1][j]) % m
                    res[i][j] = (res[i][j] + a[i][1] * a[0][j]) % m
        else:
            for i in range(2):
                for j in range(2):
                    res[i][j] = (res[i][j] + a[i][0] * a[0][j] * 2) % m
                    res[i][j] = (res[i][j] + a[i][0] * a[1][j]) % m
                    res[i][j] = (res[i][j] + a[i][1] * a[0][j]) % m
                    res[i][j] = (res[i][j] + a[i][1] * a[1][j]) % m
        return res
    
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