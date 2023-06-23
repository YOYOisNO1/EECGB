def program125():
    n, p, t = map(float, input().split())
    n = int(n)
    t = int(t)
    s = 0
    z = []
    for i in range(0,n+1):
        z.append(0)
    z[0] = 1
    for i in range(1,t+1):
        for j in range(n,-1,-1):
            if j > 0 and j < n:
                z[j] = (z[j-1]*p+z[j]*(1-p))
            elif j == n:
                z[j] = z[j-1]*p + z[j]
            else:
                z[j] = z[j]*(1-p)
        print z
    
    for i in range(1,n+1):
        s+=i*z[i]
    
    print s