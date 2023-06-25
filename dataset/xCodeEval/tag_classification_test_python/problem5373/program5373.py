def program5373():
    import sys;input=sys.stdin.readline
    M = 10**9+7
    T, = map(int, input().split())
    for _ in range(T):
        N, K = map(int, input().split())
        if N%2:
            print(pow(pow(2, N-1, M)+1, K, M))
        else:
            R = 0
            x = pow(2, N-1, M)-1
            mm = pow(2, N, M)
    #        print(x,K)
            for i in range(K):
                R += pow(x, i, M)*pow(mm, K-i-1, M)%M
                R %= M
            R+=pow(x, K, M)
            print(R%M)
    