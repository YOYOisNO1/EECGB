def program6035():
    l, r = map(int, input().strip().split())
    
    p = 1 << 64
    p -= 1
    ans = 0
    while p > 0:
        v = l ^ p
        if l <= v and v <= r:
            ans = max(ans, p)
        v = r ^ p
        if l <= v and v <= r:
            ans = max(ans, p)
        p = (p + 1) // 2
        p -= 1
    
    print(ans)