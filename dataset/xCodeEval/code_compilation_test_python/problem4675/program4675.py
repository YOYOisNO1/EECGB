    MOD,fact=10**9+7,[1]*(2*10**6+5)
    for i in range(1, len(fact)): fact[i]=(fact[i-1]*i)%(MOD)
def C(n,k):
        return (fact[n]*pow(fact[k],MOD-2,MOD)**2)%MOD
    n=input()+1
    print C(2*n,n)-1