def program924():
    n, m = map(int, input().split())
    x = []
    ans = [0] * n
    for i in range(m):
        s, d, c = map(int, input().split())
        x.append([d - 1, s - 1, c, i + 1])
        ans[d - 1] = m + 1
    x.sort()
    for d, s, c, i in x:
        cnt = 0
        while cnt < c:
            if s == d:
                print(-1)
                exit()
            if ans[s] == 0:
                ans[s] = i
                cnt += 1
            s += 1
    print(*ans)