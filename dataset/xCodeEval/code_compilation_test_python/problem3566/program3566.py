def program3566():
    C, Ha, Hb, Wa, Wb = (int(x) for x in input().split())
    
    if Ha * Wb > Hb * Wa:
        Ha, Hb, Wa, Wb = Hb, Ha, Wb, Wa
    
    res = 0
    for x in xrange(0, Wb):
        r = x * Ha + (C - x * Wa) / Wb * Hb
        res = max(r, res)
        
    print res
        