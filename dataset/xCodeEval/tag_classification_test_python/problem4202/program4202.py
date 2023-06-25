def program4202():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    
    sumA = sum(a)
    
    res = 0
    
    while round(sumA / n + 1e-13) < k:
        sumA += k
        n += 1
        res += 1
    
    print(res)