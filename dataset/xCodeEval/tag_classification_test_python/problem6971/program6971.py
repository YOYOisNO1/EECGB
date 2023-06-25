def program6971():
    prob = lambda n, k: (k*(k-1)*(k-2)/6 + k*(k-1)/2*(n-k) + (n-k)*(n-k-1)/2*k/2) / (n*(n-1)*(n-2)/6)
    EPS = 1e-8
    
    N, P = input().split()
    N = int(N); P = float(P)
    
    for k in range(0,N+1):
        p = prob(N, k)
        if p+EPS >= P:
            print(k)
            exit(0)