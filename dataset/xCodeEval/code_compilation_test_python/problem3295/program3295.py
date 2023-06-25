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
        ptrA = 0
        ptrB = 0
        ans = 0
        while ptrA < len(a) and ptrB < len(b):
            if a[ptrA] < b[ptrB]:
                ptrA += 1
                ans += 1
            elif a[ptrA] > b[ptrB]:
                ptrB += 1
                ans += 1
            else:
                ptrA += 1
                ptrB += 1
    
    print(ans)