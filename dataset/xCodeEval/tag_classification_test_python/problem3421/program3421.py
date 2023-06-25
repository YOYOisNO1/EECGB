def program3421():
    n, m = input().split()
    n = int(n)
    m = int(m)
    if m > n:
        print(-1)
        exit()
    mini = n / 2 + n % 2
    k = mini / m
    if k * m < mini:
        k += 1
    print(k) * m