def dis(ax,ay,bx,by):
        return abs(ax-bx)*abs(ax-bx) + abs(ay-by)*abs(ay-by)
    
    ar=map(int,input('').split())
    ax=ar[0]
    ay=ar[1]
    bx=ar[2]
    by=ar[3]
    cx=ar[4]
    cy=ar[5]
    
    if (cy-by)*(bx-ax)==(by-ay)*(cx-bx) or dis(ax,ay,bx,by)!=dis(bx,by,cx,cy):
        print('No')
    else:
        print('Yes')