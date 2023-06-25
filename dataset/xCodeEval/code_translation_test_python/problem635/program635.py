def program635():
    m = []
    for i in range(10):
        s = input()
        m.append(s)
    for i in range(10):
        for j in range(6):
            s = ''
            s += m[i][j] + m[i][j+1] + m[i][j+2] +m[i][j+3] + m[i][j+4]
            if s.count('X') == 4 and s.count('O') == 0:
                print('YES')
                exit()
    for i in range(10):
        for j in range(6):
            s = ''
            s += m[j][i] + m[j+1][i] + m[j+2][i] + m[j+3][i] + m[j+4][i]
            if s.count('X') == 4 and s.count('O') == 0:
                print('YES')
                exit()
    for i in range(6):
        for j in range(6):
            s = ''
            s += m[j][i] + m[j+1][i+1] + m[j+2][i+2] + m[j+3][i+3] + m[j+4][i+4]
            if s.count('X') == 4 and s.count('O') == 0:
                print('YES')
                exit()
    for i in range(6):
        for j in range(6):
            s = ''
            s += m[j+4][i] + m[j+3][i+1] + m[j+2][i+2] + m[j+1][i+3] + m[j][i+4]
            if s.count('X') == 4 and s.count('O') == 0:
                print('YES')
                exit()
    print('NO')