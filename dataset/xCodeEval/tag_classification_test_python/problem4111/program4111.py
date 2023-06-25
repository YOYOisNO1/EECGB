def program4111():
    N, M = map(int, input().split())
    T = [[] for i in range(N)]
    for i in range(N):
        t = input()
        T[i] = t
    
    R = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    S = [["."] * M for j in range(N)]
    for i in range(N):
        for j in range(M):
            flag = True
            for dx, dy in R:
                nx, ny = i + dx, j + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    flag = False
                    break
                if T[nx][ny] == ".":
                    flag = False
                    break
            if flag:
                for dx, dy in R:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        S[nx][ny] = "#"
    
    flag1 = True
    for i in range(N):
        for j in range(M):
            if T[i][j] != S[i][j]:
                flag1 = False
    
    
    if flag1:
        print("YES")
    else:
        print("NO")