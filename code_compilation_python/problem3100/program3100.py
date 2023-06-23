    import math
    
def powerMo(a,n,mo):
        ans = 1
        posi = a
        while n > 0:
            if n&1:
                ans *= posi
                ans %= mo
            n >>= 1
            posi = posi*posi%mo
        return ans
    
def modInv(a,mo):
        # return a's mod inv
        phi = mo - 1
        return(powerMo(a,phi-1,mo))
    
    
def combMo(n,a,mo):
        # Cna
        numer = 1
        for i in range(n-a+1,n+1):
            numer *= i
            numer %= mo
        denom = 1
        for i in range(1,a+1):
            denom *= i
            denom %= mo
        denomInv = modInv(denom,mo)
        ans = numer*denomInv%mo
        return ans
    
def f():
        mo = 998244353
        n, m = [int(s) for s in input().split()]
        if n==2:
            print(0)
            return
        c = combMo(m, n-1, mo)
        c *= (n-2)
        a = powerMo(2,n-3,mo)
        res = a*c%mo
        print(res)
    
    
    f()