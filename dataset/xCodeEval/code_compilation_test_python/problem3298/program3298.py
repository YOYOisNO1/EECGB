def primeFactorize(n):
        factors = []
        div = 2
        while n > 1:
            while n % div == 0:
                factors.append(div)
                n //= div
            div += 1
        return factors
    
    a,b = [primeFactorize(int(x)) for x in input().split()]
    ans = -1
    
    if a[-1] <= 5 and b[-1] <= 5:
        a2, a3, a5 = 0, 0, 0
        b2, b3, b5 = 0, 0, 0
    
        for i in a:
            if i==2: a2 += 1
            if i==3: a3 += 1
            if i==5: a5 += 1
        for i in b:
            if i==2: b2 += 1
            if i==3: b3 += 1
            if i==5: b5 += 1
        
        ans = abs(a2-b2) + abs(a3-b3) + abs(a5-b5)
    
    print(ans)