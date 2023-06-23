def program2798():
    from sys import stdin,stdout
    from math import gcd, ceil, sqrt
    ii1 = lambda: int(stdin.readline().strip())
    is1 = lambda: stdin.readline().strip()
    iia = lambda: list(map(int, stdin.readline().strip().split()))
    isa = lambda: stdin.readline().strip().split()
    mod = 1000000007
    
    l, d, v, g, r = iia()
    t = d / v
    if t % (g + r) >= g:
        t += g + r - t
    t += (l - d) / v
    print(t)