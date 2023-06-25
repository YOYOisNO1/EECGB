def program6510():
    import math
    n, m = map(int, input().split())
    f = [0] * (n + 1)
    ans = 1
    sum = [0]
    k = int(math.log2(n))
    tmp = [0] * (int(k+1) * m)
    for i in range(1, k + 1):
        sum.append(sum[-1])
        for j in range(1, m + 1):
            if tmp[i * j] == 0:
                sum[-1] += 1
                tmp[i * j] = 1
    for i in range(2, n + 1):
        if f[i] == 1:
            continue
        now, v = i, 0
        while now <= n:
            f[now] = 1
            now *= i
            v += 1
        ans += sum[v]
    print(ans)