def f(a, b):
        if b == 1:
            return a
        if b % 2 == 0:
            x = f(a, b // 2) % m
            return (x * x) % m
        else:
            return (f(a, b - 1) * a) % m
    
    n, m = map(int, input().split())
    print((f(3, n) - 1) % m)