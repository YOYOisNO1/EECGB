def program4526():
    a, b, m, r = map(int, input().split())
    for i in range(m):
        r = (a * r + b) % m
    x = (a * r + b) % m
    i = 1
    while x != r:
        x = (a * x + b) % m
        i += 1
    print(i)