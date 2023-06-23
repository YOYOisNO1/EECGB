def program2205():
    n,k = map(int,input().split())
    a = map(int,input().split())
    q = [0 for i in range(n+1)]
    h = [0 for i in range(n+1)]
    f = 1
    c = 0
    for i in range(k-1):
        if a[i+1]<=a[i]:
            if h[n-a[i]+a[i+1]] and q[a[i]]!=n-a[i]+a[i+1]:
                f = 0
                break
            q[a[i]] = n-a[i]+a[i+1]
            h[n-a[i]+a[i+1]] = 1
        else:
            if h[a[i+1]-a[i]] and q[a[i]]!=a[i+1]-a[i]:
                f = 0
                break
            q[a[i]] = a[i+1]-a[i]
            h[a[i+1]-a[i]] = 1
    u = []
    pt = 0
    for i in range(1,n+1):
        if not h[i]:
            u.append(i)
    if f:
        for i in range(1,n+1):
            if not q[i]:
                q[i] = u[pt]
                pt +=1
            print q[i],
    else:
        print -1