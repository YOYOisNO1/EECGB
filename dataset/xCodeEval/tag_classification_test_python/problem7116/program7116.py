    p, k = map(int, input().split())
    
def solve(p, k):
        mod = 10 ** 9 + 7
        if k == 1:
            return pow(p, p, mod)
        if k == 0:
            return pow(p, p-1, mod)
        ps = [k * x % p for x in range(p)]
        n_groups = 0
        visited = [0] * p
        visited[0] = 1
        for x, px in enumerate(ps):
            if visited[x]:
                continue
            n_groups += 1
            y = px
            while visited[y] == 0:
                visited[y] = 1
                y = ps[y]
        return pow(p, n_groups, mod)
    
    print(solve(p, k))