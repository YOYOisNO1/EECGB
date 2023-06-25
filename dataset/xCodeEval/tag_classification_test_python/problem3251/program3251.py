def program3251():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    b = [[] for i in range(2*10**5+1)]
    for i in l:
        cnt = 0
        while i:
            b[i].append(cnt)
            cnt += 1
            i //= 2
    ans = 1e15
    for x in b:
        if len(x) >= k:
            x = sorted(x)
            ans = min(ans, sum(x[:k]))
    print(ans)