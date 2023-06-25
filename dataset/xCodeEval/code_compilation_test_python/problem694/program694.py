    #!/usr/bin/python3
    
    import functools
    
def gcd(x, y):
        while(y):
            y, x = x % y, y
        return x
    
def prime_factors(n):
        if (n === 1):
            return [ 1 ]
        i = 2
        factors = []
        while (i * i <= n):
            if (n % i):
                i += 1
            else:
                while (n % i == 0):
                    n /= i
                factors.append(i)
    
        if (n > 1):
            factors.append(n)
        return factors
    
    factors = prime_factors(int(input()));
    print(functools.reduce(lambda r, i: gcd(r, i), factors[1:], factors[0]));