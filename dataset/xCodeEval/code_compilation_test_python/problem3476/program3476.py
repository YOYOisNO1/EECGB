def program3476():
    (r, g, b) = [int(x) for x in input().split()]
    
    r = (r + 1) / 2 * 3 - 3
    g = (g + 1) / 2 * 3 - 2
    b = (b + 1) / 2 * 3 - 1
    
    print 30 + max(0, r, g, b)