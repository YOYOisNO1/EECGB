    n = int(input())
    a = list(map(int, input()))
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    p = [0] * 10
    p[0] = 4, 2
    p[1] = 1, 1
    p[2] = 1, 2
    p[3] = 1, 3
    p[4] = 2, 1
    p[5] = 2, 2
    p[6] = 2, 3
    p[7] = 3, 1
    p[8] = 3, 2
    p[9] = 3, 3
    path = []
    for i in range(1, n):
        dx = p[a[i]][0] - p[a[i - 1]][0]
        dy = p[a[i]][1] - p[a[i - 1]][1]
        path.append((dx, dy))
    
def go(x, y, i):
        if i == n - 1:
            print('NO')
            exit()
        nx, ny = x + path[i][0], y + path[i][1]
        if 1 <= nx <= 4 and 1 <= ny <= 3 and b[nx - 1][ny - 1] != -1:
            go(nx, ny, i + 1)
        
    for x, y in p:
        if b[x - 1][y - 1] != a[0] and b[x - 1][y - 1] != -1:
            go(x, y, 0)
    print('YES')