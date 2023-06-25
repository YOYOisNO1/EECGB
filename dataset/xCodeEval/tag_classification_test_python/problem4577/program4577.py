def program4577():
    n, m, k = map(int, input().split())
    
    if k < n:
        print(k + 1, 1)
    
    else:
        t = k - n
        vert = t // (m - 1)
        hor = t % (m - 1)
    
        print(n - vert, [m - hor, hor + 2][1 - (vert % 2)])