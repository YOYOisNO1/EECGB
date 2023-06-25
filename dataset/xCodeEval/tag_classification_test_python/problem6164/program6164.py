    import sys
    
    stdin = sys.stdin
    inf = 1 << 60
    mod = 1000000007
    
    ni      = lambda: int(ns())
    nin     = lambda y: [ni() for _ in range(y)]
    na      = lambda: list(map(int, stdin.readline().split()))
    nan     = lambda y: [na() for _ in range(y)]
    nf      = lambda: float(ns())
    nfn     = lambda y: [nf() for _ in range(y)]
    nfa     = lambda: list(map(float, stdin.readline().split()))
    nfan    = lambda y: [nfa() for _ in range(y)]
    ns      = lambda: stdin.readline().rstrip()
    nsn     = lambda y: [ns() for _ in range(y)]
    ncl     = lambda y: [list(ns()) for _ in range(y)]
    nas     = lambda: stdin.readline().split()
    
    from collections import deque
    
    x, y, gx, gy = na()
    x -= 1
    y -= 1
    gx -= 1
    gy -= 1
    h, w = 8, 8
    
def bfs(ty):
        q = deque()
        q.append((x, y))
        dist = [[inf] * w for _ in range(h)]
        dist[y][x] = 0
        while len(q):
            p = q.popleft()
            cx, cy = p
            if ty == "rook":
                dx = [0, 1, -1, 0]
                dy = [1, 0, 0, -1]
                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    while nx >= 0 and nx < w and ny >= 0 and ny < h:
                        if dist[ny][nx] == inf:
                            dist[ny][nx] = dist[cy][cx] + 1
                            q.append((nx, ny))
                        nx, ny = nx + dx[i], ny + dy[i]
            elif ty == "bishop":
                dx = [1, -1, -1, 1]
                dy = [-1, 1, -1, 1]
                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    while nx >= 0 and nx < w and ny >= 0 and ny < h:
                        if dist[ny][nx] == inf:
                            dist[ny][nx] = dist[cy][cx] + 1
                            q.append((nx, ny))
                        nx, ny = nx + dx[i], ny + dy[i]
            elif ty == "king":
                # (1, 1) (1, 0) (1, -1) (0, -1) (-1, -1) (-1, 0) (-1, 1) (0, 1)
                dx = [1, 1, 1, 0, -1, -1, -1, 0]
                dy = [1, 0, -1, -1, -1, 0, 1, 1]
                for i in range(8):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if nx >= 0 and nx < w and ny >= 0 and ny < h and dist[ny][nx] == inf:
                        dist[ny][nx] = dist[cy][cx] + 1
                        q.append((nx, ny))
        return dist[gy][gx] if dist[gy][gx] != inf else 0
    
    print(bfs("rook"), bfs("bishop"), bfs("king"))