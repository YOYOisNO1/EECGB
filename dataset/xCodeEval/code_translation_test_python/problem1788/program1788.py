def program1788():
    n, C = map(int, input().split())
    fac = [1]
    z = 1000003
    for i in range(1, 700000):
        fac.append((fac[-1] * i) % z)
    ans = 0
    for i in range(1, n+1):
        x = (fac[i+C-1] * pow(fac[i], z-2, z) * pow(fac[C-1], z-2, z)) % z
        ans = (ans + x) % z
    print(ans)