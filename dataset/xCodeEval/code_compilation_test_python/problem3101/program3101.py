def program3101():
    M = 998244353
    n, m = map(int, input().split())
    f = [1]*(m+1)
    for i in range(m):
        f[i+1] = f[i]*(i+1)%M
    
    cc = 0
    if n > 2: cc = f[m]*(n-2)*pow(2,n-3,M)*pow(f[n-1]*f[m-n+1],M-2, M)
    print(cc%M)