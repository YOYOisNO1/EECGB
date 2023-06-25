def program4640():
    M, N = 998244353, 720720
    I = lambda: [int(x) for x in input().split()]
    p = [0]*(N+1)
    res = 0
    
    n, a, x, y, k, U = I()
    for i in range(1, n+1):
        p[a%N] += 1
        res += a//N * N
        a = (a * x + y) % U
    
    res = (res * pow(n, k-1, M) * k) % M
    for i in range(1, k+1):
        tot = sum(p[j]*j for j in range(1, N+1))
        for j in range(1, N + 1):
            t1 = p[j]
            p[j] *= (n-1)
            p[j - j%i] += t1
        res += (tot * pow(n, k-i)) % M
    
    print(res % M)