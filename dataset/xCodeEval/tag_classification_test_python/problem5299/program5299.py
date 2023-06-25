def program5299():
    ##import random
    ##n = 10
    ##u = list(range(1, n + 1))
    ##random.shuffle(u)
    ##print(*u)
    ##while True:
    ##    x = int(input())
    ##    p = u[:x]
    ##    p.reverse()
    ##    u = p + u[x:]
    ##    print(*u)
    
    n, m = map(int, input().split())
    sumL = [0] * (n + 2)
    L = [0] * (n + 1)
    L[-1], sumL[-2] = 1, 1
    for i in range(n - 1, 0, -1):
        L[i] = sumL[i + 1]
        j = 2
        while i * j <= n:
            L[i] += (sumL[i * j] - sumL[min(n, (i + 1) * j - 1) + 1])
            j += 1
        L[i] = L[i] % m
        sumL[i] = (sumL[i + 1] + L[i]) % m
    print(L[1])