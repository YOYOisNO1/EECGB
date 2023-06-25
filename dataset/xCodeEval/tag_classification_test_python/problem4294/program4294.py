def bad(x, y, t):
        x1, y1 = x, y + t
        return 0 <= 8 - y1 < 8 and 0 <= x1 < 8 and a[8 - y1][x1] == "S" or 0 <= 7 - y1 < 8 and 0 <= x1 < 8 and a[7 - y1][x1] == "S"
    
    dp = [[[False] * 30 for i in range(8)] for j in range(8)]
    a = []
    for i in range(8):
        a.append(input().rstrip())
    
    dp[0][0][0] = True
    for t1 in range(29):
        for x in range(8):
            for y in range(8):
                if dp[x][y][t1]:
                    for i in [(x + 1, y), (x - 1, y), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x, y + 1), (x, y - 1), (x, y)]:
                        if 0 <= i[0] < 8 and 0 <= i[1] < 8:
                            if not bad(i[0], i[1], t1 + 1):
                                dp[i[0]][i[1]][t1 + 1] = True
    
    for i in range(30):
        if dp[7][7][i]:
            print("WIN")
            exit()
    print("LOSE")