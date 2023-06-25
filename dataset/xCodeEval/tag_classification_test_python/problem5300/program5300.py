def program5300():
    n, M = map(int, input().split())
    factors = [[] for _ in range(n+1)]
    for d in range(2, n // 2+1):
        for q in range(2*d, n+1, d):
            factors[q].append(d)
    ans = [0, 1]
    d = [0, 0]
    p = 1
    for i in range(2, n+1):
        d.append((d[-1] + 1 + sum(ans[i//x] - ans[i//x-1] for x in factors[i])) % M)
        ans.append((p + d[-1]) % M)
        p = (p + ans[-1]) % M
    print(ans[-1])