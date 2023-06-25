def program3374():
    a, m = map(int, input().split())
    print("Yes" if (2 ** 50 * (a % m)) % m == 0 else "No")