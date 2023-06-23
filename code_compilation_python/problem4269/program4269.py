def program4269():
    l = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
    s = [[int(i) for i in input().split()],
         [int(i) for i in input().split()],
         [int(i) for i in input().split()]]
    for i in range(3):
        for j in range(3):
            if s[i][j] % 2 != 0:
                if l[i][j]:
                    l[i][j] = 0
                else:
                    l[i][j] = 1
                if i > 0:
                    if l[i-1][j]:
                        l[i-1][j] = 0
                    else:
                        l[i-1][j] = 1
                if i < 2:
                    if l[i+1][j]:
                        l[i+1][j] = 0
                    else:
                        l[i+1][j] = 1
                if j > 0:
                    if l[i][j-1]:
                        l[i][j-1] = 0
                    else:
                        l[i][j-1] = 1
                if j < 2:
                    if l[i][j+1]:
                        l[i][j+1] = 0
                    else:
                        l[i][j+1] = 1
    for i in range(3):
        for j in range(3):
            print(l[i][j], end='')
        print()