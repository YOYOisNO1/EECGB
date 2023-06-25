def program6777():
    n = int(input())
    m = int(1e9 + 7)
    u, v = 0, 1
    for _ in range(n - 1):
        u, v = v, (u + v + 2) % m
    print(v)