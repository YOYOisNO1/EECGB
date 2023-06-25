def is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
        a1 = y2 - y1
        b1 = x1 - x2
    
        a2 = y4 - y3
        b2 = x3 - x4
    
        # Parallel = determinant is 0
        return not (a1 * b2 - a2 * b1)
    
    
    if __name__ == '__main__':
        n = int(input())
        carr = [tuple(map(int, input().split())) for _ in range(4 * n + 1)]
    
        xs = list(map(lambda o: o[0], carr))
        ys = list(map(lambda o: o[1], carr))
    
        # find bounds first
        lx, rx = min(xs), max(xs)
        dy, uy = min(ys), max(ys)
    
        # detect if outlier is outside the box
        for x in [lx, rx]:
            if xs.count(x) == 1:
                print(*carr[xs.index(x)])
                exit(0)
    
        for y in [dy, uy]:
            if ys.count(y) == 1:
                print(*carr[ys.index(y)])
                exit(0)
    
        # find outlier inside the box
        ur = rx, uy
        dl = lx, dy
    
        for x, y in carr:
            # check if line formed by point with ur is parallel to x/y -axis
            # or line formed by point with dl is parallel to x/y -axis
            lur = x, y, *ur
            ldl = x, y, *dl
    
            if not (is_parallel(*lur, 0, 0, 0, 1)
                    or is_parallel(*lur, 0, 0, 1, 0)
                    or is_parallel(*ldl, 0, 0, 0, 1)
                    or is_parallel(*ldl, 0, 0, 1, 0)):
                print(x, y)
                break