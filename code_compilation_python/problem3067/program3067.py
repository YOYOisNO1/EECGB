def can(n, m, k):
        if n % 2 == 0:
            return False
        d = 1
        while d*d <= m:
            if m % d == 0 and (d in range(k, m) or m/d in range(k, m)):
                return True
            d += 1
        return False
    
    n, m, k = map(int, input().split(' '))
    print ('Timur' if can(n, m, k) else 'Marsel')