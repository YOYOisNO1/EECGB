def program324():
    dc = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m, d = map(int, input().split())
    print((dc[m] + d + 5) // 7)