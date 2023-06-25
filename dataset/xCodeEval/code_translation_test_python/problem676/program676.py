def C(n, m):
        r = 1
        for i in range(n - m + 1,n + 1): r *= i
        for i in range(1, m + 1): r //= i
        return r
    n, k = map(int, input().split())
    a = 0
    for i in range (1, n + 1):
        t = 1
        l = i
        for j in range(2, i + 1):
            s = 0
            while not l % j:
                s += 1
                l //= j
            if s:
                t *= C(s + k - 1, s)
        a += t
    print(a % (10 ** 9 + 7))