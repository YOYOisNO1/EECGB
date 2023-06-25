def program4508():
    n, m =  map(int, input().split())
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        f[i] = f[i - 1]  * i % m
    ans = 0
    for i in range(n):
        ans += (n - i) * (n - i) * f[i + 1] * f[n - i - 1] % m
    print(ans) % m