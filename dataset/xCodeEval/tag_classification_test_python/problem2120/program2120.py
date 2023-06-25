def program2120():
    bignum = 10**9+7
    n, k, d = [int(i) for i in input().split()]
    D = [[0 for j in range(2)] for i in range(n+1)]
    D[0][0] = 1
    for i in range(1, n+1):
        for j in range(1,k+1):
            if i < j:
                break
            if j < d:
                D[i][0] += D[i-j][0]
                D[i][1] += D[i-j][1]
                D[i][0] %= bignum
                D[i][1] %= bignum
            else:
                D[i][1] += D[i-j][0] + D[i-j][1]
                D[i][1] %= bignum
    print(D[n][1])