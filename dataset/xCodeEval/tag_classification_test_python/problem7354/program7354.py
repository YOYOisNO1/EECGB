def program7354():
    n, m = map(int, input().split())
    if n >= 4 and m >= 4:
        print(n * m - (n * m % 2))
    else:
        if min(n, m) == 1:
            if max(n, m) % 6 == 5:
                print(max(n, m) // 6 * 6 + 4)
            elif max(n, m) % 6 == 4:
                print(max(n, m) // 6 * 6 + 2)
            else:
                print(max(n, m) // 6 * 6)
        elif min(n, m) ==  2 and max(n, m) == 7:
            print(12)
        elif min(n, m) == 2 and max(n, m) >= 4 or min(n, m) == 3 and max(n, m) >= 4:
            print(n * m - (n * m % 2))
        else:
            d = [[0, 0, 0, 2, 4], [0, 0, 4, 8, 10], [0, 0, 8, 12, 14], [0, 0, 0, 16, 20], [0, 0, 0, 0, 24]]
            print(d[min(n, m) - 1][max(n, m) - 1])