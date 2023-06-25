def program6874():
    if __name__ == "__main__":
        n = int(input())
        # 3 types of coins: 4, 9, 49; total <= n
        # case 1: no 4
        # there can be at most 13 * 9
        # THIS INCLUDES 0
        if n >= 13:
            result = (n - 12) * 14 + 7 * 13
        else:
            result = (n + 1) * (n + 2) / 2
        # case 2: with 4
        # case 2.1: no 49
        # at most 4 * 9 and 8 * 4
        if n >= 12:
            result += 40
        else:
            result += [0, 1, 3, 6, 10, 15, 20, 25, 30, 34, 37, 39, 40][n]
        # case 2.2: with 4 & 49
        # at most 4 * 9 and 7 * 4
        if n >= 12:
            result += (n - 6) * 35
        else:
            result += [0, 0, 1, 4, 10, 20, 35, 55, 80, 109, 141, 175, 210][n]
        print(result)