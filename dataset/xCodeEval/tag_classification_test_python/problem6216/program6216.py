    x1, y1, x2, y2 = map(int, input().split())
    n = 8
    
    
def check(x):
        return 1 <= x <= n
    
    
def get_nbs_sl(x, y):
        for i in range(-8, 9):
            a, b = x + i, y + i
            c, d = x - i, y + i
            if i == 0:
                continue
    
            if check(a) and check(b):
                yield (a, b)
    
            if check(c) and check(d):
                yield (c, d)
    
    
def get_nbs_ld(x, y):
        for i in range(1, n + 1):
            if i != x:
                yield (i, y)
        for i in range(1, n + 1):
            if i != y:
                yield (x, i)
    
    
def get_nbs_king(x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if (nx, ny) != (x, y) and check(nx) and check(ny):
                    yield (nx, ny)
    
    
def bfs(start_x, start_y, fin_x, fin_y, get_nbs):
        dist = {(start_x, start_y): 0}
        q = [(start_x, start_y)]
        while q:
            v = q.pop(0)
            # print(v)
            for u in get_nbs(v[0], v[1]):
                if u not in dist:
                    dist[u] = dist[v] + 1
                    q.append(u)
        if (fin_x, fin_y) in dist:
            return dist[(fin_x, fin_y)]
        else:
            return 0
    
    
    ld = bfs(x1, y1, x2, y2, get_nbs_ld)
    sl = bfs(x1, y1, x2, y2, get_nbs_sl)
    kk = bfs(x1, y1, x2, y2, get_nbs_king)
    
    print(ld, sl, kk)