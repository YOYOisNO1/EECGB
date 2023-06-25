    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    
    import sys
    
    MAXN = 110
    MOD = 10 ** 9 + 7
    INF = MOD
    
def MakeCom():
        global com
        com = [[1]]
        for i in xrange(1, MAXN + 1):
            line = [1]
            for j in xrange(1, i):
                line.append((com[-1][j - 1] + com[-1][j]) % MOD)
            line.append(1)
            com.append(line)
    
def ReadIn():
        data = [int(x) for x in sys.stdin.read().split()]
        offset = 0
        while offset < len(data):
            n, cap = data[offset : offset + 2]
            offset += 2
            friends = [0] * 2
            for x in data[offset : offset + n]:
                friends[x / 50 - 1] += 1
            offset += n
            yield cap, tuple(friends)
    
def merge(x, y):
        if y[0] < x[0]:
            return y
        elif y[0] > x[0]:
            return x
        else:
            return tuple([x[0], (x[1] + y[1]) % MOD])
    
def DFS(remain, cap, f, total):
        if remain in f:
            return f[remain]
        if remain[0] + 2 * remain[1] <= cap:
            f[remain] = (1, 1)
            return f[remain]
        f[remain] = (INF, 0)
        for x in xrange(remain[0] + 1):
            if x > cap: break;
            for y in xrange(remain[1] + 1):
                if x + y < 1: continue;
                if x + 2 * y > cap: break;
                tmp = [remain[0] - x, remain[1] - y]
                for i in xrange(2):
                    if tmp[i] == total[i]: continue
                    tmp[i] += 1
                    nextRem = tuple(tmp)
                    if nextRem != remain:
                        ret = DFS(nextRem, cap, f, total)
                        global com
                        ret = tuple([ret[0] + 2,
                            com[remain[0]][x] * com[remain[1]][y] * (total[i] - nextRem[i] + 1) * ret[1] % MOD])
                        f[remain] = merge(f[remain], ret)
                    tmp[i] -= 1
        return f[remain]
    
def Solve(cap, friends):
        cap /= 50
        f = {(0, 0) : (0, 1)} 
        ans = list(DFS(friends, cap, f, friends))
        if ans[0] == INF: ans[0] = -1
        for x in ans: print x
    
    if __name__ == '__main__':
        MakeCom()
        for cap, friends in ReadIn():
            Solve(cap, friends)