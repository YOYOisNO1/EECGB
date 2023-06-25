def program1122():
    # cf 851 A 800
    n, k, t = map(int, input().split())
    
    standing = min(k, n)
    standing = min(t, k) # at start
    if t > n:
        # 5 - (12 - 10) = 5 - 2
        visible = max(0, k - (t - n))
        standing = min(standing, visible)
    print(standing)