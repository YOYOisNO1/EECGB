def program2619():
    n, m, mw = map(int, input().split())
    mw += 1
    we = list(map(int, input().split()))
    ce = list(map(int, input().split()))
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v -1)
        graph[v-1].append(u-1)
    used = [False] * n
    w = []
    c = []
    for i in range(n):
        if not used[i]:
            stack = [i]
            res = []
            resc = []
            while stack:
                cur = stack.pop()
                used[cur] = True
                res.append(we[cur])
                resc.append(ce[cur])
                for u in graph[cur]:
                    if not used[u]:
                        stack.append(u)
            res.append(sum(res))
            resc.append(sum(resc))
            w.append(res)
            c.append(resc)
    m = 0
    F = [[0] * mw for i in range(len(w))]
    for i in range(len(w)):
        for k in range(mw):
            for g in range(len(w[i])):
                if k >= w[i][g]:
                    F[i][k] = max(F[i - 1][k], F[i - 1][k - w[i][g]] + c[i][g], F[i][k])
                else:
                    F[i][k] = max(F[i][k], F[i-1][k-1])
    print(F[-1][-1])