def program4356():
    n, k = [int(i) for i in input().split()]
    for i in range(k - 1, 0, -1):
        if n % i == 0:
            print((n // i)*k + i)
            break