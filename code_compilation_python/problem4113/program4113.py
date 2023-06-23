def program4113():
    (p, k) = map(int, input().split())
    used = [0] * p
    if k == 0:
        print(pow(p, p - 1) % (10 ** 9 + 7))
    else:
        c = 1 if k == 1 else 0
        for x in range(1, p):
            if not used[x]:
                y = x
                while not used[y]:
                    used[y] = True
                    y = k * y % p
                c += 1
        print(pow(p, c) % (10 ** 9 + 7))