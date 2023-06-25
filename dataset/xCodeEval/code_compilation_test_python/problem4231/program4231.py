    
def gcd(a, b):
    	return a if b == 0 else gcd(b, a % b)
    
    n, m, x, y, a, b = map(int, input().strip().split())
    g = gcd(a, b)
    a /= g
    b /= g
    s = min(n / a, m / b)
    a *= s
    b *= s
    x1 = x - (a + 1) / 2
    y1 = y - (b + 1) / 2
    x2 = x1 + a
    y2 = y1 + b
    
    print x1, y1, x2, y2