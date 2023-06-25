def program4719():
    n = int(input())
    res = [0,0,0]
    maxi = [0,0,0]
    for i in range(3):
        a, b = map(int, input().split())
        res[i] = a
        maxi[i] = b
        n -= a
    
    for i in range(3):
        if n > 0:
            mini = min(n,maxi[i] - res[i])
            res[i] += mini
            n -= mini
    
    print(*res)