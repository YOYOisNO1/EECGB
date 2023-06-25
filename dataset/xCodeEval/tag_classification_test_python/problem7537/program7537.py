def check(a, b, c):
        return (b <= a and a < c)
def can(n, m, k):
        if n % 2 == 0:
            return False
        d = 1
        while d*d <= m:
            if m % d == 0 and (check(d, k, m) or check(m/d, k, m)):
                return True
            d += 1
        return False
    
    n, m, k = map(int, input().split(' '))
    print(('Timur') if can(n, m, k) else 'Marsel')