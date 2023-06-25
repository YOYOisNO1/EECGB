def program1511():
    c, hr, hb, wr, wb = map(int, input().split())
    if c<wr:
        print(c/wb*hb)
    elif c<wb:
        print(c/wr*hr)
    else:
        v1 = 1.0*hr/wr
        v2 = 1.0*hb/wb
        if v1<v2:
            wtemp = wr
            htemp = hr
            wr = wb
            hr = hb
            wb = wtemp
            hb = htemp
        joy = 0
        
        for i in xrange(wr+1):
            if c-i*wb<0:
                break
            joy = max(joy, i*hb+(c-i*wb)/wr*hr)
    
        print(joy)