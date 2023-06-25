def program3477():
    n, m = list(map(int, input().split(' ')))
    ans = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            if (i*i + j*j) % m == 0:
                ans += ((n - i) // m + 1) * ((n - j) // m + 1)
    print(ans)