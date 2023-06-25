    __author__ = 'MoonBall'
    
    import sys
    # sys.stdin = open('data/D.in', 'r')
    T = 1
    M = 1000000007
    
def process():
        P, K = list(map(int, input().split()))
        k = [K * x % P for x in range(P)]
    
        # print(k)
        # f(0) = k[f(0)]
        # f(1) = k[f(4)]
        # f(2) = k[f(3)]
        # f(3) = k[f(2)]
        # f(4) = k[f(1)]
    
        if not K:
            print(pow(P, P - 1, M))
            return
        if K == 1:
            print(pow(P, P, M))
            return
    
        f = [0] * P
        c = [0] * P
        ans = 1
        for i in range(P):
            if f[i]: continue
    
            cnt = 1
            u = i
            f[u] = 1
            while not f[k[u]]:
                u = k[u]
                f[u] = 1
                cnt = cnt + 1
    
            c[cnt] = c[cnt] + 1
    
        # print(c)
        for i in range(2, P):
            if c[i] != 0:
                cnt = i * c[i] + 1
                ans = ans * pow(cnt, c[i], M) % M
    
        print(ans)
    
    
    
    
    
    
    
    
    for _ in range(T):
        process()