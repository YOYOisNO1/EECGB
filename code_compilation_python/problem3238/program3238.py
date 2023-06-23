def program3238():
    n=input()
    m=[map(int, input().split() for i in [0]*n]
    print sum( m[i][j] for i in range(n)
        for j in range(n)
            if i == j or i == n-j-1 or i == n/2 or j == n/2)