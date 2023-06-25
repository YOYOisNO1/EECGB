def program1305():
    import sys
    import math
    import cProfile
     
    DEBUG = False
    
    if DEBUG:
        sys.stdin = open('input.txt')
        pr = cProfile.Profile()
        pr.enable()
     
    n = sys.stdin.readline()
    n = int(n)
     
    # Init global variables.
    points = []
     
    for i in range(4 * n + 1):
        x, y = sys.stdin.readline().split()
        points.append((int(x), int(y)))
    
    for k in range(4 * n + 1):
        p = points[:]
        del p[k]
    
        x_cnt = {}
        y_cnt = {}
        for i in range(4 * n):
            x_cnt[p[i][0]] = x_cnt.get(p[i][0], 0) + 1
            y_cnt[p[i][1]] = y_cnt.get(p[i][1], 0) + 1
    
        x_v = x_cnt.values()
        y_v = y_cnt.values()
        if x_v[0] == 3 and x_v[-1] == 3 and y_v[0] == 3 and y_v[-1] == 3:
            break
    
    print(points[k])
    
    if DEBUG:
        pr.disable()
        pr.print_stats()