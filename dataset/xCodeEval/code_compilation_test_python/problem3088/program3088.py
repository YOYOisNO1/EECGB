def program3088():
    
    
    input()
    
    digs = set()
    for x in input():
        digs.add(int(x))
    
    # if 2 in digs and 0 in digs:
    #     print 'NO'
    
    xs = [(x - 1) % 3 for x in digs if x != 0]
    ys = [(x - 1) / 3 for x in digs if x != 0]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    
    if maxx - minx >= 2 and maxy - miny >= 2:
        print 'YES'
    else:
        print 'NO'
    
    