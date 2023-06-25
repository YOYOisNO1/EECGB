def program6088():
    a, b, c, d = map(int, input().split())
    print(((d - b) // 2 + 1) * (c - a + 1) - (c - a) // 2)