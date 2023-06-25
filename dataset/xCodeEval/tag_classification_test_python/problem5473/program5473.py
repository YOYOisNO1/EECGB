def program5473():
    n, h = map(int, input().split())
    
    ceq = [[0] * (n + 1) for i in range(n + 1)]
    cle = [[0] * (n + 1) for i in range(n + 1)]
    ceq[0][0] = 1
    cle[0] = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(n):
            for left in range(i):
                ceq[i][j + 1] += ceq[left][j] * cle[i - left - 1][j] + cle[left][j] * ceq[i - left - 1][j] - ceq[left][j] * ceq[i - left - 1][j]
            cle[i][j + 1] = cle[i][j] + ceq[i][j + 1]
    print(cle[n][n] - cle[n][h - 1])