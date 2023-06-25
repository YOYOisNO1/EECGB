def solve():
        mod = int(1e9+7)
        n, m, k = map(int, input().split())
        if k==1 or k>n:
            print(pow(m, n, mod))
        elif k==n:
            print(pow(m, (n+1)//2, mod))
        elif k%2==1:
            print((m*m)%mod)
        elif k%2==0:
            print(m)
    solve()