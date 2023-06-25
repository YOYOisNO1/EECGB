    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = map(int,input().split())
    x5,y5,x6,y6 = map(int,input().split())
    
def dl(x1,x2,x3,x4):
        l = [x1,x2,x3,x4]
        cp = l[:]
        if sorted(cp)==l or sorted(cp)==l[2:]+l[:2]:
            return 0
        else:
            return abs(min(x2,x4)-max(x1,x3))
    
def tl(x1,x2,x3,x4,x5,x6):
        if dl(x1,x2,x3,x4)==0 or dl(x1,x2,x5,x6)==0 or dl(x5,x6,x1,x2)==0:
            return 0
        return abs(min(x2,x4,x6)-max(x1,x3,x5))
    
    wa = (x2-x1)*(y2-y1)
    s = (dl(x1,x2,x3,x4)*dl(y1,y2,y3,y4)+dl(x1,x2,x5,x6)*dl(y1,y2,y5,y6))-(tl(x1,x2,x3,x4,x5,x6)*tl(y1,y2,y3,y4,y5,y6))
    #print(wa,s)
    if s>=wa:
        print('NO')
    else:
        print('YES')