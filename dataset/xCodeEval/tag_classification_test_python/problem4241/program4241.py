def program4241():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print((max(2, abs(a - c) + 1) + max(2, abs(b - d) + 1)) * 2)