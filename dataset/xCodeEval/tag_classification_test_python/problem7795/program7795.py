    import sys
    
    n = int(sys.stdin.readline())
    
    line = sys.stdin.readline().split()
    t = [int(line[i]) for i in range(n)]
    
    covered = set()
    seenRoots = set()
    
def cover(rootx, rooty, angle, depth, t, covered):
        if depth == n:
            return
        if (rootx, rooty, angle, depth) in seenRoots:
            return
    
        newx = rootx
        newy = rooty
        for i in range(t[depth]):
            if angle == 0:
                newy += 1
            elif angle == 1:
                newx += 1
                newy += 1
            elif angle == 2:
                newx += 1
            elif angle == 3:
                newx += 1
                newy -= 1
            elif angle == 4:
                newy -= 1
            elif angle == 5:
                newx -= 1
                newy -= 1
            elif angle == 6:
                newx -= 1
            elif angle == 7:
                newx -= 1
                newy += 1
            covered.add((newx, newy))
    
        seenRoots.add((rootx, rooty, angle, depth))
        cover(newx, newy, (angle - 1) % 8, depth + 1, t, covered)
        cover(newx, newy, (angle + 1) % 8, depth + 1, t, covered)
    
    cover(0, 0, 0, 0, t, covered)
    print(len(covered))