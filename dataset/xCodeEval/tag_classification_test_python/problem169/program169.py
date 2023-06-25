def lcm(a,b):
        m = a*b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return m // (a+b)
    import math
    n,m,z = map(int, input().split())
    print(z //lcm(n, m))