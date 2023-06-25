def program2053():
    n, k, d = map(int,input().split())
    z = [[1], [1]]
    for i in range(1, n + 1):
        z[0].append(sum(z[0][max(i-d+1, 0):]))
        z[1].append(sum(z[1][max(i-k, 0):]))
    print((z[1][-1] - z[0][-1]) % (10**9+7))