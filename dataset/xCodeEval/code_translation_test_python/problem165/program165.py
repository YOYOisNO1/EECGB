def program165():
    n, m = map(int, input().split())
    
    idx = 0
    while (idx * (idx - 1) // 2) < m:
        idx += 1
    
    print(max(0, n - m * 2), max(0, n - idx))