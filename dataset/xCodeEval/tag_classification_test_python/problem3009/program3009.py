def program3009():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(a) - sum(a[-k:]) + k * x)