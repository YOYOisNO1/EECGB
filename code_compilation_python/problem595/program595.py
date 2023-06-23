    n = int(input())
    
def f(a, b, c):
        return (a + 1) * (b + 2) * (c + 2) - a * b * c
    
    Smax = f(n, 1, 1)
    
    from math import sqrt
    Smin = Smax
    for a in range(1, int(sqrt(n)) + 1):
        if n % a != 0:
            continue
        for i in range(1, int(sqrt(n / a)) + 1):
            if (n / a) % i == 0:
                Smin = min(Smin, f(a, i, (n / a) / i))
    
    print Smin, Smax