def program4160():
    h, m, s, t1, t2 = map(int, input().split())
    a = [0] * 43200
    a[(h * 3600 + 60 * m + s) % 43200] = 1
    a[(m * 720 + 12 * s) % 43200] = 1
    a[(s * 720) % 43200] = 1
    a[(t2 * 3600) % 43200] = 2
    possible = False
    for i in range(t1 * 3600, t1 * 3600 + 43200):
        if a[i % 43200] == 1:
            break
        elif a[i % 43200] == 2:
            possible = True
            break
    for i in range(t1 * 3600, t1 * 3600 - 43200, -1):
        if a[i % 43200] == 1:
            break
        elif a[i % 43200] == 2:
            possible = True
            break
    if possible:
        print("Yes")
    else:
        print("No")