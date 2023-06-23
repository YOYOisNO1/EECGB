def program2212():
    n = int(input())
    mod = 1000000007
    d = []
    d.append(0)
    d.append(3)
    d.append(6)
    d.append(21)
    d.append(60)
    for i in range(3,n):
        d.append((7*(d[i-2]%mod))%mod + (6*(d[i-3]%mod))%mod)%mod)
    print d[n-1]
        