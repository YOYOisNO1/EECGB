    mod = 10**9+7
    import math
    
def sieve(n): 
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n): 
            if (prime[p] == True): 
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
        return prime
    
def factor(n):
        # limit = int(math.sqrt(n)+1)
        fac={i:0 for i in range(n+1)}
        i=2
        while(n>1):
            if not prime[i]:
                i+=1
                continue
            if n%i==0:
                fac[i]+=1
                n=n//i
            else:
                i+=1
            # print(n,' ')
        return {i:fac[i] for i in fac if fac[i]!=0}
    
    
    
    
    
def ncr(n, r, p=mod):
        num = den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den,
                          p - 2, p)) % p
    
    n,k = list(map(int,input().split()))
    
    prime = sieve(n)
    # print([i for i in range(len(prime)) if prime[i]])
    # print(factor(5))
    
    final = 0
    for num in range(2,n+1):
        fac = factor(num)
        # print('n = ',num)
        ans = 1
        for a in fac:
            part = ncr(fac[a]+k-1,k-1)
            ans = (ans * part)%mod
            # print(part,a,fac[a])
        final = (ans+final)%mod
    print((final+1)%mod)