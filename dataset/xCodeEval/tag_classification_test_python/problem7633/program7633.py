def f(m, cnt, y):
        global ans, x
        if m == 0:
            ans, x = max((ans, x), (cnt, y))
            return
        a = 1
        while (a + 1) ** 3 <= m: a += 1
        f(m - a ** 3, cnt + 1, y + a ** 3)
        if a >= 1: f(a ** 3 - (a - 1) ** 3 - 1, cnt + 1, y + (a - 1) ** 3)
    
    m = int(input())
    ans, x = 0, m
    f(m, 0, 0)
    print(ans, x)