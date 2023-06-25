def program2225():
    m = []
    for i in range(11):
        s = input().split()
        if i == 3 or i == 7:
            continue
        m += [s]
    matrix = []
    for i in m:
        cur = ""
        for j in i:
            cur += j
        matrix.append(cur)
    for i in range(9):
        matrix[i] = list(matrix[i])
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    field = [x % 3, y % 3]
    cnt = 0
    for i in range(field[0] * 3, field[0] * 3 + 3):
        for j in range(field[1] * 3, field[1] * 3 + 3):
            cnt += (matrix[i][j] == ".")
    if cnt == 0:
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == ".":
                    matrix[i][j] = "!"
    else:
        for i in range(field[0] * 3, field[0] * 3 + 3):
            for j in range(field[1] * 3, field[1] * 3 + 3):
                if matrix[i][j] == ".":
                    matrix[i][j] = "!"
    for i in range(9):
        for j in range(9):
            if j == 2 or j == 5:
                print(matrix[i][j], end=" ")
            else:
                print(matrix[i][j], end="")
        print()
        if i == 2 or i == 5:
            print()