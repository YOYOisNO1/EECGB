def program1705():
    n, k, m, d = map(int, input().split())
    ans = 0
    for i in range(1, d + 1):
        x = min(n // ((i - 1) * k + 1), m)
        if (x && (n // x + k - 1) // k == i):
            ans = max(ans, x * i);
    print(ans)