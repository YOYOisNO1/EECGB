    MOD = 10**9+7
    
    fact = [1]*2000004
    for i in range(1,2000004):
        fact[i] = (fact[i-1]*i)%MOD
    inv = [1]*2000004
    for i in range(2,2000004):
        inv[i] = (-(MOD//i)*inv[MOD%i])%MOD
    for i in range(2,2000004):
        inv[i] = (inv[i]*inv[i-1])%MOD
def C(n,k):
        return (fact[n]*inv[k]*inv[n-k])%MOD
    x=int(input())+1
    res = C(x*2,x)-1
    print(res)