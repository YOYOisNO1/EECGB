def program3572():
    __author__ = 'MatFuck'
    
    import sys
    
    #sys.stdin = open("1.txt")
    
    m = input()
    
    a = [int(x) for x in input().split()]
    
    [x_c, y_c] = [int(x) for x in input().split() ]
    
    x = 0
    x_i = -1
    y = 0
    y_i = m
    
    while (x < x_c) and (x_i < m):
        x_i += 1
        x += a[x_i]
    
    if x_i == m:
        print 0
        sys.exit(0)
    
    
    while y < x_c and y_i > x_i:
        y_i -= 1
        y += a[y_i]
    
    if y_i <= x_i:
        print 0
        sys.exit(0)
    
    while x_i + 1 < y_i:
        if (x < y):
            x_i += 1
            x += a[x_i]
        else:
            y_i -= 1
            y += a[y_i]
    
    if (x_c <= x) and (x <= y_c) and (x_c <= y) and (y <= y_c):
        print x_i + 2
    else:
        print 0