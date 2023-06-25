def program155():
    mod = 10**9 + 7
    
    n, m = map(int, input().strip().split())
    
    F = [0, 1]
    for i in range(2, 100002):
        F.append(F[i - 1] + F[i - 2])
        F[i] %= mod
    
    res = 2 * ((F[m + 1] + F[n + 1] - 1)) % mod
    print(res)