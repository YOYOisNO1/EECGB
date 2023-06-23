def program947():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        mod = int(1e9+7)
        p = pow(2,n-1,mod)
        b = 1
        c = 1
        if n%2 == 0: b = p
        else: b = p+1
        m = (2*p)%mod
        for i in range(2,k+1):
            c = (c*m)%mod
            if n%2 == 0: b = (c+((p-1)*b)
            else: b = ((p+1)*b)
        if k == 0: print(1)
        else: print(b%mod)