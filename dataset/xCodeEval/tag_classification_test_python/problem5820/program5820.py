def program5820():
    n = int(input()) - 1
    
    L = 0
    R = n + 1
    while (L + 1 != R):
        M = (L + R) // 2
        if (M * (M + 1) // 2 <= n):
            L = M
        else:
            R = M
    n -= L * (L + 1) // 2
    print(n + 1)
    