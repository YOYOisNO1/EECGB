def program1988():
    mod = 10**9+7
    n, k, d = map(int, input().strip().split())
    notD = [0 for i in range(n+1)]
    notD[0] = 1
    withD = [0 for i in range(n+1)]
    withD[0] = 1
    
    for i in range(n+1):
        for j in range(1, d):
            if i >= j:
                notD[i] += notD[i-j]
    
    
    for i in range(n+1):
        for j in range(1, k+1):
            if i >= j:
                withD[i] += withD[i-j]
    
    # print(withD)
    # print(notD)
    print((withD[n]-notD[n])%mod)