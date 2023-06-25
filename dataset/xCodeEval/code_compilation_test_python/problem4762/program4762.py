def program4762():
    a, b, m = map(int, input().split())
    t = [0] * m
    s = 10 ** 9 % m
    for i in range(a):
        k = i * s % m
        if 0 < k < m - b: exit(print(1, str(i).zfill(9)))
        if t[k]: break
        t[k] = 1
    print(2)