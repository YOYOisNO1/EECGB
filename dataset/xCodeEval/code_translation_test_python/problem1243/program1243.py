def program1243():
    n, m, s = map(int, input().split())
    r = n % s
    c = m % s
    if r == 0:
        r = s
    if c == 0:
        c = s
    r *= (n - 1) / s + 1
    c *= (m - 1) / s + 1
    print(r) * c