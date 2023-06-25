def program712():
    n, m, k = map(int, input().split())
    a = map(int, input().split())
    a = sorted (a,reverse = True)
    currentSocketsCount = k
    if m <= k:
        return 0
    else:
        for i in xrange(n):
            currentSocketsCount += a[i]-1
            if currentSocketsCount >= m:
                print i+1
                break
            if i == n-1 and currentSocketsCount < m:
                print -1
    
    