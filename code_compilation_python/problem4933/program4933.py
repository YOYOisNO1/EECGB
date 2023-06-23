def program4933():
    fact = [1]*1000000
    mod = 10**6+3
    for i in range(2,1000000):
        fact[i] = (i*fact[i-1])%mod
    n,c = map(int,input().split())
    ans = fact[n+c]*pow(fact[c],mod-2,mod)*pow(fact[n],mod-2,mod)
    print ((ans-1)%mod+mod)%mod