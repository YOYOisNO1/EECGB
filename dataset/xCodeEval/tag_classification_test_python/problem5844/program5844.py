def gcd(a, b):
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        return b
    
    
def factorize(t, n):
        count = 0
        while t % n == 0:
            count += 1
        return count
    
    
def factorize23(t):
        count2 = 0
        count3 = 0
    
        while t % 2 == 0:
            count2 += 1
            t /= 2
    
        while t % 3 == 0:
            count3 += 1
            t /= 3
    
        if t != 1:
            print(-1)
            exit(0)
    
        return count2 + count3, count3
    
    
def eat(a, b, count2, count3):
        while a % 3 == 0 and count3 > 0:
            count3 -= 1
            a = a * 2 / 3
        while b % 3 == 0 and count3 > 0:
            count3 -= 1
            b = b * 2 / 3
        while a % 2 == 0 and count2 > 0:
            count2 -= 1
            a /= 2
        while b % 2 == 0 and count2 > 0:
            count2 -= 1
            b /= 2
        return a, b
    
    
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    
    g = gcd(a1 * b1, a2 * b2)
    
    t12, t13 = factorize23(a1 * b1 / g)
    t22, t23 = factorize23(a2 * b2 / g)
    
    a1, b1 = eat(a1, b1, t12 - t22, t13)
    a2, b2 = eat(a2, b2, t22 - t12, t23)
    
    print(t13) + t23 + abs(t12 - t22)
    print(a1,) b1
    print(a2,) b2