def program1987():
    n, k, d = map(int, input().split())
    b=10**9+7
    ways = [0] * (n + 1)
    ways.insert(0, 0)
    j = 1
    s = 0
    while (j <= min(k,n)):
        ways[j] = 1
        j += 1
    s += ways[n]
    for i in range(2, n + 1):
        new_ways = [0] * (n + 1)
        for j in range(1, n + 1):
            for p in range(1, k + 1):
                if (j + p) <= n:
                    new_ways[j + p] += ways[j]
        ways = []
        for j in new_ways:
            ways.append(j)
        s += (ways[n])
        s=s%b
    ways = [0] * (n + 1)
    ways.insert(0, 0)
    j = 1
    r = 0
    while (j <= min(d-1,n)):
        ways[j] = 1
        j += 1
    r += ways[n]
    for i in range(2, n + 1):
        new_ways = [0] * (n + 1)
        for j in range(1, n + 1):
            for p in range(1, d):
                if (j + p) <= n:
                    new_ways[j + p] += ways[j]
        ways = []
        for j in new_ways:
            ways.append(j)
        r += (ways[n])
        r=r%b
    
    print((s - r)%b)