def program87():
    a, bm, f, k = [int(i) for i in input().split()]
    b = bm
    r1, r2 = f, a - f
    count = 0
    for i in range(k):
        b -= r1
        if b < 0:
            print(-1)
            exit(0)
        if b < 2 * r2 and i != k - 1:
            b = bm
            count += 1
        elif i == k - 1:
            if b < r2:
                b = bm
                count += 1
        b -= r2
        if b < 0:
            print(-1)
            exit(0)
        r1, r2 = r2, r1
    print(count)