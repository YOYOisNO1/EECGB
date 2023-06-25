    
    
def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
def my_gcd(fact, mm):
        # print("my_gcd",fact,mm)
        res = 1
        for i in fact:
            if mm % i == 0:
                mm = mm // i
                res = res * i
        # print("my_gcd", res)
        return res
    
def solve(n,k,a,b):
        qq = [a+b,a-b,-a-b,-a+b]
        mini=n*k
        maxi = 0
    
        factN = prime_factors(n)
        fact = factN + prime_factors(k)
    
        m = n*k
        for q in qq:
            for t in range(1,n+1):
                mm = t*k + q
                if mm > 0:
                    x = my_gcd(fact, mm)
                    # print(x)
                    y = m//x
                    if y < mini:
                        mini = y
                    if y > maxi:
                        maxi = y
        return mini, maxi
    
    
    n,k = input().split()
    n = int(n)
    k = int(k)
    
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    x,y = solve(n,k,a,b)
    print(x,y)