def program1647():
    n, m = map(int, input().split())
    print(max(min((m + 1) // 2 - 1, n - m // 2), 0))