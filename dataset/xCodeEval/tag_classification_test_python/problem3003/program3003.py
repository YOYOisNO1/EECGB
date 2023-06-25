def program3003():
    String =[[0 for i in range(5)] for j in range(5)]
    for i in range(1,4): String[i][1:4] = [int(x)%2 for x in input().split()]
    for i in range(1,4):
        for j in range(1,4): print((1+String[i][j] + String[i-1][j]+String[i+1][j]+String[i][j-1]+String[i][j+1])%2, end='')
        print()