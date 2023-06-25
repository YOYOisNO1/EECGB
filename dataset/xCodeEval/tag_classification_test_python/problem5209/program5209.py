def program5209():
    from sys import stdin
    mod = 998244353
    a = [1,1,1]
    n = int(stdin.readline())
    while len(a)<n+1:
        a.append(a[-1] + a[-2])
        if a[-1] >=mod:
            a[-1]-=mod
    den = pow(2,mod-2,mod)
    den = pow(den,n,mod)
    print((a[n]*den)%mod)