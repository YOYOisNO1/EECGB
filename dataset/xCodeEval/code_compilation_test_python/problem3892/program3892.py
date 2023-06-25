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
        for toX in xrange(remain[0] + 1):
            if toX > cap: break
            for toY in xrange(remain[1] + 1):
                if toX + toY < 1: continue
                if toX + 2 * toY > cap: break
                arrival = total[0] - remain[0] + toX, total[1] - remain[1] + toY
                for backX in xrange(arrival[0] + 1):
                    if backX > cap: break;
                    for backY in xrange(arrival[1] + 1):
                        if backX + backY < 1: continue
                        if backX + 2 * backY > cap: break
                        nextRemain = remain[0] - toX + backX, remain[1] - toY + backY
                        ret = DFS(nextRemain, cap, f, total)
                        global com
                        ret = tuple([ret[0] + 2,
                                    com[remain[0]][toX] * com[remain[1]][toY] *
                                    com[arrival[0]][backX] * com[arrival[1]][backY] *
                                    ret[1] % MOD])
                        f[remain] = merge(f[remain], ret)
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