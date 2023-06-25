def program5598():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if 0 in (i, j):
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j] + a[i][j - 1]
    print(a[n) - 1][n - 1]