def dfs(i, j):
        if a[i][j] != -1:
            return a[i][j]
        d1 = dfs(i - 1, j - 1) + (s1[i - 1] == s2[j - 1]) * s1[i - 1]
        d2 = dfs(i - 1, j)
        d3 = dfs(i, j - 1)
        a[i][j] = max(d1, d2, d3, key=lambda x: [len(x), -x.count(virus)])
        return a[i][j]
    
    s1, s2, virus = input(), input(), input()
    #s1, s2, virus = 'SLO', 'LL', 'asda'
    n1, n2 = len(s1), len(s2)
    a = [[''] * (n2 + 1)] + [[''] + [-1] * n2 for i in range(n1)]
    
    #a[1][0] = 'hjkhj'
    ans = dfs(n1, n2)
    while virus in ans:
        ans = min(ans.replace(virus, virus[:-1]), ans.replace(virus, virus[1:]), key=lambda x: x.count(virus))
    print(0 if ans == '' else ans)