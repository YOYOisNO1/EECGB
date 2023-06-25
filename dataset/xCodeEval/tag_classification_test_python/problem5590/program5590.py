def is_good(matrix):
        for i in range(10):
            for j in range(10):
                if matrix[i][j] == 'X':
                    if matrix[i][j - 2] == matrix[i][j - 1] == matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2] or \
                                                            matrix[i - 2][j] == matrix[i - 1][j] == matrix[i][j] == \
                                            matrix[i + 1][j] == matrix[i + 2][j]:
                        return True
                    for k in range(4):
                        if matrix[i - k][j - k] == matrix[i - k + 1][j - k + 1] == matrix[i - k + 2][j - k + 2] == \
                                matrix[i - k + 3][j - k + 3] == matrix[i - k + 4][j - k + 4]:
                            return True
                        if matrix[i - k][j + k] == matrix[i - k + 1][j + k - 1] == matrix[i - k + 2][j + k - 2] == \
                                matrix[i - k + 3][j + k - 3] == matrix[i - k + 4][j + k - 4]:
                            return True
        return False
    
    
    matrix = [['.'] * 14 for i in range(14)]
    
    for i in range(10):
        string = input()
        for j in range(10):
            matrix[i][j] = string[j]
    
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == '.':
                matrix[i][j] = 'X'
                if is_good(matrix):
                    print('YES')
                    exit()
                matrix[i][j] = '.'
    print('NO')