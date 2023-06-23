def program4382():
    n = int(input())
    a = [0] * n
    b = 0
    a[0] = 1
    if n > 1:
        a[1] = 2
    for i in range(2, n):
        a[i] = a[i - 2] + a[i - 1] + 1
    if n > 1:
        b = a[n - 2]
    print((a[n - 1] + b) % (10 ** 9 + 7))
    