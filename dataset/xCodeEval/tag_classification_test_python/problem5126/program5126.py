    from math import log2, trunc
    
    
def lo(n):
        i = 0
        while 2 ** i <= n:
            i += 1
        return i
    
    
def f(n, l, r):
        if n <= 1:
            return n
        m = 2 ** lo(n) - 1
        if l < m // 2 + 1 and r < m // 2 + 1:
            return f(n // 2, l, r)
        if l > m // 2 + 1 and r > m // 2 + 1:
            return f(n // 2, l - m // 2 - 1, r - m // 2 - 1)
        if l < m // 2 + 1 < r:
            return f(n // 2, l, m // 2) + n % 2 + f(n // 2, 1, r - m // 2 - 1)
        if l == m // 2 + 1 == r:
            return n % 2
        if l == m // 2 + 1:
            return n % 2 + f(n // 2, 1, r - m // 2 - 1)
        if r == m // 2 + 1:
            return n % 2 + f(n // 2, l, m // 2)
    
    
    n, l, r = map(int, input().split())
    s = 0
    print(f(n, l, r))