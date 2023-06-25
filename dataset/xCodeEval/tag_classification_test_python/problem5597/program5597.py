def program5597():
    n = int(input())
    a = []
    if n ==1:
        print(1)
        exit()
    for i in range(n):
        a.append([1] * n)
    for i in range(n):
        for j in range(n):
            if (i != 0) and (j != 0):
                a[i][j] = a[i-1][j] + a[i][j-1]
    print(a[n-1][n-1])