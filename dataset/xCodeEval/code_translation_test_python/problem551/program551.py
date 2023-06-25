def followSpiral(pt):
        if pt == (0, 0): return 0
        if pt == (1, 0): return 0
        if pt == (1, 1): return 1
        corners = [pp, np, nn, pn] = [(1, 1), (0, 0), (0, 0), (1, 0)]
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        outer = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        turns, count, pos, corner =  2, 0, pp, 1, 
        while True:
            count += 1
            x, y = pos
            dx, dy = dirs[corner]
            pos = x+dx, y+dy
            if pos == pt: break
            cx, cy = corners[corner]
            ox, oy = outer[corner]
            if pos == (cx+ox, cy+oy):
                turns += 1
                corners[corner] = (cx+ox, cy+oy)
                corner = (corner+1)%4
        return turns
    
    # IO:
    inp = input()
    pt = tuple(map(int, inp.split(' ')))
    print(followSpiral(pt))