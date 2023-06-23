    
    
def egcd(a, b):
        if b == 0:
            return 1, 0, a
        x1, y1, c = egcd(b, a % b)
        return y1, x1 - (a / b) * y1, c
    
def crt(a0, n0, a1, n1):
        if min(n0, n1) < 0:
            return 0, -1
        x, y, g = egcd(n0, n1)
        if (a0 - a1) % g:
            return 0, -1
        x *= (a1 - a0) / g
        y *= (a1 - a0) / g
        k = n1 * n0 / g
        return (n0 * x + a0) % k, k
    
    
    
    a, b, p, x = map(int, input().split())
    ans = 0
    for i in range(p - 1):
        a1 = pow(a, i * (p - 2), p) * b
        a0, n0 = crt(a1, p, i, p - 1)
        if x >= a0:
            ans += 1 + (x - a0) / n0
    print(ans)