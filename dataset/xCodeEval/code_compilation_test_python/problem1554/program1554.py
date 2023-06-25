    import sys
    
    n = int(input().strip())
    
    hsides = []
    vsides = []
    xranges = {}
    yranges = {}
    
    for i in range(n):
        x1, y1, x2, y2 = [int(i) for i in input().strip().split()]
        if y2 - y1 == x2 - x1:
            print("YES")
            sys.exit(1)
        vside1 = [x1, y1, y2, "left"]
        vside2 = [x2, y1, y2, "right"]
        hside1 = [y1, x1, x2, "bottom"]
        hside2 = [y2, x1, x2, "top"]
        if y1 not in yranges:
            yranges[y1] = []
        yranges[y1].append([x1, x2])
        if y2 not in yranges:
            yranges[y2] = []
        yranges[y2].append([x1, x2])
        if x1 not in xranges:
            xranges[x1] = []
        xranges[x1].append([y1, y2])
        if x2 not in xranges:
            xranges[x2] = []
        xranges[x2].append([y1, y2])
    
def inrange(start, end, ranges, index):
        if index not in ranges:
            return False
        for r in ranges[index]:
            if r[0] <= start and r[1] >= end:
                return True
        return False
    
    for side in vsides:
        s = side[2]-side[1]
        if side[3] == "left":
            topok = inrange(side[0]-s, side[0], yranges, side[2])
            bottomok = inrange(side[0]-s, side[0], yranges, side[1]) 
            newleftok = inrange(side[1], side[2], xranges, side[0]-s)
            ok = topok and bottomok and newleftok
        if side[3] == "right":
            topok = inrange(side[0], side[0]+s, yranges, side[2])
            bottomok = inrange(side[0], side[0]+s, yranges, side[1]) 
            newrightok = inrange(side[1], side[2], xranges, side[0]+s)
            ok = topok and bottomok and newrightok
        if side[3] == "top":
            leftok = inrange(side[0], side[0]+s, xranges, side[1])
            rightok = inrange(side[0], side[0]+s, xranges, side[2])
            newtopok = inrange(side[1], side[2], yranges, side[0]+s)
            ok = leftok and rightok and newtopok
        if side[3] == "bottom":
            leftok = inrange(side[0]-s, side[0], xranges, side[1])
            rightok = inrange(side[0]-s, side[0], xranges, side[2])
            newbottomok = inrange(side[1], side[2], yranges, side[0]-s)
            ok = leftok and rightok and newbottomok
        if ok:
            print("YES")
            sys.exit(1)
    print("NO")