def program2111():
    n, k, d = map(int,input().split())
    mod = 10**9 + 7
    add = [0]*105; sub = [0]*105
    add[0] = sub[0] = 1
    for i in range(n+1):
        for p in range(min(n-i, k)):
            add[p+i+1] = (add[p+i+1] + add[i])%mod
        for q in range(min(n-i, d-1)):
            sub[q+i+1] = (sub[q+i+1] + sub[i])%mod
    print((add[n] - sub[n] + mod)%mod)