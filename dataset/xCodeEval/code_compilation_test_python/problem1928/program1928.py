def program1928():
    n, m = map(int, input().split())
    
    overlap = min(n / 3, m / 2)
    
    print min(max(2 * n, 3 * (m + overlap)), max(2 * (n + overlap), 3 * m))
    
    # if 2 * n < 3 * m:
    #     # 2s go higher than 3s
    #     print max(2 * n, 3 * m + 3 * (n / 2))
    # else:
    #     #3s go higher than 2s
    #     print max(3 * m, 2 * n + m)