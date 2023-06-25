def program1105():
    import sys
    
    ctl = [[1 for x in range(3)] for x in range(3)]
    
    for x in range(3):
        li = [int(z) for z in sys.stdin.readline().split()]
        for y in range(3):
            ctl[x][y] = (ctl[x][y] + li[y]) % 2
            if x-1 >= 0:
                ctl[x-1][y] = (ctl[x-1][y] + li[y]) % 2
            if y-1 >= 0:
                ctl[x][y-1] = (ctl[x][y-1] + li[y]) % 2
            if y+1 <= 2:
                ctl[x][y+1] = (ctl[x][y+1] + li[y]) % 2
            if x +1 <= 2:
                ctl[x+1][y] = (ctl[x+1][y] + li[y]) % 2
    
    for x in range(3):
        print('').join([str(y) for y in ctl[x]]) 