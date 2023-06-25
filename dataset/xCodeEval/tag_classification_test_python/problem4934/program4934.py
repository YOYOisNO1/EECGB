def program4934():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    p = n//2
    q = n-p
    B = A[0:p]
    C = A[p:n]
    
    S = []
    for i in range(2**p):
        s = 0
        for j in range(p):
            if (i >> j) & 1:
                s += B[j]
        s %= m
        S.append(s)
    
    T = []
    for i in range(2**q):
        t = 0
        for j in range(q):
            if (i >> j) & 1:
                t += C[j]
        t %= m
        T.append(t)
    
    T.sort()
    ans = -1
    import bisect
    for s in S:
        idx = bisect.bisect_right(T, m-1-s)
        if idx != 0:
            ans = max(ans, max((s+T[idx-1])%m, (s+T[-1])%m))
        else:
            ans = max(ans, (s+T[-1])%m)
    print(ans)