    import sys
    import math
    
def stoc(s):
        return tuple(map(int, s.split()))
    
def ncut(c0, c1):
        d2 = (c0[0]-c1[0])**2 + (c0[1]-c1[1])**2
        rsum2 = (c0[2]+c1[2])**2
        if rsum2 < d2:
            return 0
        elif rsum2 == d2:
            return 1
        else:
            #d = |r0 - r1| ?
            rdiff2 = (c0[2]-c1[2])**2
            if d2 < rdiff2:
                return 0
            elif d2 == rdiff2:
                return 1
            else:        
                return 2
    
def testcuts(cs):
        N=10**10
        eps=1e-8
        ai = 0
        while ai < N:
            a = 2*math.pi*ai/N+.1
            x = cs[0][0] + cs[0][2]*math.cos(a)
            y = cs[0][1] + cs[0][2]*math.sin(a)
            d1 = abs(((x-cs[1][0])**2 + (y-cs[1][1])**2)**.5 - cs[1][2])
            d2 = abs(((x-cs[2][0])**2 + (y-cs[2][1])**2)**.5 - cs[2][2])
            #print(x,) y, d1, d2
            if abs(d1) + abs(d2) < eps:
                #print(x,) y, d1, d2
                return True
            steps = min(d1, d2) / cs[0][2]
            ai += 1
            ai += int(N*steps/10)
        return False
            
    xx = sys.stdin.readlines()
    n = int(xx[0])
    cs = map(stoc, xx[1:])
    #print(cs)
    
    if n == 1:
        print(2)
        sys.exit(0)
    if n == 2:
        print(2) + max(ncut(cs[0], cs[1]), 1)
        sys.exit(0)
    
    ncuts = ncut(cs[0],cs[1]) + ncut(cs[1],cs[2]) + ncut(cs[2], cs[0])
    
    if ncuts == 0:
        print(4)
        sys.exit(0)
        
    #print(ncut(cs[0],cs[1]),) ncut(cs[1],cs[2]), ncut(cs[2], cs[0])
    
    if ncut(cs[0], cs[1]) == 0 and ncut(cs[1],cs[2]) == 0:
        ncuts += 1
    if ncut(cs[0], cs[1]) == 0 and ncut(cs[2],cs[0]) == 0:
        ncuts += 1
    if ncut(cs[0], cs[2]) == 0 and ncut(cs[1],cs[2]) == 0:
        ncuts += 1
    
    #Do all three intersect at the same point?
    if ncuts >=3 and testcuts(cs):
        ncuts -= 1
        #two cuts and all three in same line?
        if ncuts>3 and (cs[0][0] - cs[1][0])*(cs[0][1] - cs[2][1]) == (cs[0][1] - cs[1][1])*(cs[0][0] - cs[2][0]):
            ncuts -= 1
    
    print(2) + ncuts 