def program1673():
    n, m = [int(x) for x in input().split()]
    count = 0
    mn = min(n, m)
    for a in range(0, 1000):
        for b in range(0, 1000):
            if (a * a + b == n) and (a + b * b == m):
                count += 1
    print(count)