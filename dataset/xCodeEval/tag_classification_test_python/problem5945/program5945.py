    import sys
    sys.setrecursionlimit(99999999)
    i = lambda: sys.stdin.readline().strip()
    ii = lambda: map(int, i().split())
    
    n = int(i())
    adj = map(lambda e: e-1, ii())
    visited = [0] * n
def src(e):
        if visited[e] == 2:
            return 0
        else:
            visited[e] += 1
            return visited[e] - 1 + src(adj[e])
    lengths = []
    for e in xrange(n):
        a = src(e)
        if a % 2 == 0:
            a /= 2
        if a != 0:
            lengths.append(a)
def gcd(a, b):
        if a > b: return gcd(b, a)
        elif a == 0: return b
        else: return gcd(a, b % a)
def lcm(a, b):
        return a * b / gcd(a, b)
    if 1 in visited:
        print(-1)
    else:
        print(reduce(lcm,) lengths)