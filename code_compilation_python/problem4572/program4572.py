def solve(N, M):
        if M == 0: return 1000000
        if M == 1: return N - 1
        d, r = divmod(N, M)
        return d + solve(M, r)
    
    N = int(input())
    ans = 1000000
    for M in range(1, N + 1):
        ans = min([ans, solve(N, M)])
    print(ans)