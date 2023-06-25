def program745():
    from __future__ import print_function
    n = input()
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    summa = sum(a[(n-1)//2])
    a[(n-1)//2] = [0 for i in range(n)]
    for i in range(n):
        summa+=a[i][i]
        a[i][i] = 0
        summa+=a[i][n-i-1]
        a[i][n-i-1] = 0
    for i in range(n):
        summa+=a[i][(n-1)//2]
    print(summa)