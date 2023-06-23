def program584():
    from math import factorial
        import time
        n, m = map(int, input().split())
    
        if m == 1:
            kmin = kmax = factorial(n) // (factorial(2) * factorial(n - 2))
        elif m == 2:
            if n == 2:
                kmax = kmin = 0
            elif n == 3:
                kmax = kmin = 1
            else:
                if n % 2 == 0:
                    kmin = 2 * factorial(n // 2) // (factorial(2) * factorial((n // 2) - 2))
                    kmax = factorial(n - 1 // 2) // (factorial(2) * factorial(n - 3))
                else:
                    kmin = factorial(n // 2) // (factorial(2) * factorial((n // 2) - 2)) + factorial(n // 2 + 1) // (factorial(2) * factorial((n // 2) - 1))
                    kmax = factorial(n - 1 // 2) // (factorial(2) * factorial(n - 3))
    
        else:
            x = n - m + 1
            kmax = factorial(x) // (factorial(2) * factorial(x - 2))
            if n % 2 == 1:
                kmin = 3 + (n - 3) // 2
            else:
                kmin = n // 2
    
        print(kmin, kmax)