    a,b = map(int, input().strip().split(' '))
    moves = list(input().strip())
    
    if a == 0 and b == 0:
        print("Yes")
        exit()
    
    initials = [(0,0) for _ in xrange(len(moves) + 1)]
    
    MM = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    cx, cy = (0,0)
    
    for i, tupm in enumerate(map(lambda x: MM[x], moves)):
        dx, dy = tupm
        cx += dx
        cy += dy
        initials[i + 1] = (cx, cy)
    
    BAD = -2
    ANY = -1
    
def get_cycle(destination, start, jump):
        cycle_len = BAD
        if jump == 0 and destination - start == 0:
            cycle_len = ANY
        elif jump != 0 and (destination - start) % jump == 0:
            cycle_len = (destination - start) / jump
            if cycle_len < 0:
                cycle_len = BAD
        return cycle_len
    
    for ix, iy in initials:
        xcyc = get_cycle(a, ix, cx)
        ycyc = get_cycle(b, iy, cy)
        if xcyc != BAD and ycyc != BAD and (xcyc == ANY or ycyc == ANY or xcyc == ycyc):
            print("Yes")
            exit()
    
    print("No")