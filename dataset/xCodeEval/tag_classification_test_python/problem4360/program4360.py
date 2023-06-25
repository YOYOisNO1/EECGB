def program4360():
    n, k = map(int, input().split())
    for i in range(1, n + 1):
        if n % i == 0:
            rem = n // i
            if k > rem >= 0:
                ans = i * k + rem
                break
    print(ans)