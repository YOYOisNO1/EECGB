    import sys
    import math
    from decimal import *
    
def nchoosek(n, k):
        if k == 0:
            return 1
        if n == 0:
            return 0
        if n <= 1000:
            return math.factorial(n) / math.factorial(k) / math.factorial(n-k)
        else:
            ans = 1
            ncopy = n
            for i in range(k):
                ans *= ncopy
                ncopy -= 1
            ans /= math.factorial(k)
            return ans
    
    n, m = [int(x) for x in input().strip().split()]
    
    ans = 0
    
    tot = Decimal(nchoosek(m*n-1, n-1))
    for i in range(0, min(m, n)):
        p = Decimal(nchoosek(m*(n-1), (n-1)-i) * nchoosek(m-1, i))/tot
        if p < 0.0000000001:
            break
        ans += p*(Decimal(i+1)/Decimal(n))
    
    print(ans)