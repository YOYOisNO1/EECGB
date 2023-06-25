def program2004():
    n,k,d = map(int,input().split())
    ai = [0] * (n+1)
    k = min(n,k)
    ai[0] = 1
    mode = 10 ** 9 + 7
    for i in range(1,k):
        for j in range(i):
            ai[i] += ai[j]
    for i in range(k,n+1):
        for j in range(1,k+1):
            ai[i] += ai[i - j] 
    d = min(n,d-1)
    ai2 = [0] * (n+1)
    ai2[0] = 1
    for i in range(1,d):
        for j in range(i):
            ai2[i] += ai2[j]
    for i in range(d,n+1):
        for j in range(1,d+1):
            ai2[i] += ai2[i - j]
    print((ai[n] - ai2[n]) % mode)