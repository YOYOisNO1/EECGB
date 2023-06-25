def gcd(a, b):
      return a if b == 0 else gcd(b, a % b)
    n, m, x, y, a, b = map(int, input().split())
    g = gcd(a, b)
    a /= g
    b /= g
    c = min(n / a, m / b)
    a *= c
    b *= c
    x1 = max(x - (a + 1) / 2, 0)
    y1 = max(y - (b + 1) / 2, 0)
    x2 = min(x1 + a, n)
    y2 = min(y1 + b, m)
    x1 = x2 - a
    y1 = y2 - b
    print(x1,) y1, x2, y2