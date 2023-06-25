def program217():
    n,k = map(int, input().split())
    print(6 + (n - 2) * 3 + min(n - k, k - 1))