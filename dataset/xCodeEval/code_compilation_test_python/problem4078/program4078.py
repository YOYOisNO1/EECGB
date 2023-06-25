def program4078():
    v1, v2 = sorted(map(int, input().split()))
    
    t, d = map(int, input().split())
    
    df = (v2 - v1 - 1) // d
    sm = t - 2
    
    x = (sm + df) >> 1
    y = (sm - df) >> 1
    
    ans = d * x * (x + 1) // 2
    ans += d * y * (y + 1) // 2
    
    ans += x * v1 + v1
    ans += y * v2 + v2
    
    # print(x, y)
    print(ans)