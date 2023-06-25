def program3203():
    n, m = [int(i) for i in input().split()]
    moves = [(int(x), int(y)) for x, y in (input().split() for i in range(m))]
    map = [[0 for i in xrange(n)] for j in xrange(n)]
    for i, (x, y) in enumerate(moves):
        for p in xrange(-1, 2):
            for q in xrange(-1, 2):
                try:
                    map[x+p][y+q] += 1
                    if map[x+p][y+q] >= 9:
                        print i+1
                        exit()
                except IndexError:
                    pass
    print -1