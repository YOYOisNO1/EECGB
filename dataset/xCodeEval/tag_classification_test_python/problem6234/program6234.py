def exp(x, n, rem):
        if n == 0:
            return 1
        if n % 2:
            return (x * exp(x, n - 1, rem)) % rem
        a = exp(x, n / 2, rem)
        return (a ** 2) % rem
    
    
    n = int(input())
    tri = lambda x: x * (x + 1) / 2
    rem = 10 ** 9 + 7
    res = exp(2, n, rem)
    print(tri(res)) % rem