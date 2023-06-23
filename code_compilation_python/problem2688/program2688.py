def program2688():
    s = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            q = {}
            for x in t[i].keys() | t[j].keys():
                q[x] = t[i].get(x, 0) + t[j].get(x, 0)
            ij = i * j
            for k in range(1, c + 1):
                ijk = ij * k
                if ijk in ans: s += ans[ijk]
                else:
                    y = 1
                    for x in q.keys() | t[k].keys():
                        y = y * (q.get(x, 0) + t[k].get(x, 0) + 1)
                    ans[ijk] = y
                    s += y