    from collections import deque
def main():
        n, m = map(int, input().split())
        b = [list(input().strip()) for _ in xrange(n)]
    def inboard(y, x):
            return 0 <= y < n and 0 <= x < m
        c = 0
        for i in xrange(n):
            for j in xrange(m):
                if b[i][j] in '123456789':
                    c += 1
                    b[i][j] = chr(ord(b[i][j]) - 1)
                elif b[i][j] == 'S':
                    sy, sx = i, j
        v = [int(input()) for _ in xrange(c)]
        inf = 1000000
        up = [[0] * m for i in xrange(n)]
        down = [[0] * m for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if b[i][j] in '0123456789':
                    for l in xrange(j+1, m):
                        up[i][l] |= 1 << int(b[i][j])
                        down[i][l] |= 1 << int(b[i][j])
                elif b[i][j] == 'B':
                    for l in xrange(j+1, m):
                        up[i][l] |= 1 << c
                        down[i][l] |= 1 << c
                    v.append(-inf)
                    c += 1
        dp = [[[inf] * (1 << c) for j in xrange(m)] for i in xrange(n)]
        dp[sy][sx][0] = 0
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()
        q.append((sy, sx, 0, 0))
        while q:
            y, x, mask, t = q.popleft()
            if t > dp[y][x][mask]: continue
            nt = t + 1
            for dy, dx in d:
                ny, nx, nmask = dy + y, dx + x, mask
                if not inboard(ny, nx) or b[ny][nx] not in '.S': continue
                if dx == 0:
                    if dy == 1:
                        nmask ^= down[ny][nx]
                    else:
                        nmask ^= down[y][x]
                if dp[ny][nx][nmask] > nt:
                    dp[ny][nx][nmask] = nt
                    q.append((ny, nx, nmask, nt))
        print max(sum(v[j] for j in xrange(c) if ((i >> j) & 1))-dp[sy][sx][i] for i in xrange(1 << c))
    main()