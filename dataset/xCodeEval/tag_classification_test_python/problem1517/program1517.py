    n = int(input())
    s = input()
    d = [[[-1] * (n + 1) for i in range(n + 1)] for j in range(n + 1)]
def f(a, b, c):
        if a < 0 or b < 0 or c < 0:
            return 0
        if (a, b, c) == (1, 0, 0):
            return 1
        if (a, b, c) == (0, 1, 0):
            return 2
        if (a, b, c) == (0, 0, 1):
            return 4
        if d[a][b][c] == -1:
            res = 0
            if a > 1:
                res |= f(a - 1, b, c)
            if b > 1:
                res |= f(a, b - 1, c)
            if c > 1:
                res |= f(a, b, c - 1)
            res |= f(a - 1, b - 1, c + 1) | f(a + 1, b - 1, c - 1) | f(a - 1, b + 1, c - 1)
            d[a][b][c] = res
        return d[a][b][c]
    
    p = [s.count('B'), s.count('G'), s.count('R')]
    for i in range(3):
        if p[i] > 10:
            p[i] = 3
    z = f(*p)
    RGB = 'BGR'
    print('').join([RGB[i:i+1] for i in range(3) if ((1 << i) & z)])