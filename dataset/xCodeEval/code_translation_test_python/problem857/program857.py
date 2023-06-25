    x1,y1,x2,y2,x3,y3 = map(int, input().split())
    
def isRight(a1,b1,a2,b2,a3,b3):
        if a1 == a2 and b1 == b2:
            return False
        if a1 == a3 and b1 == b3:
            return False
        if a3 == a2 and b3 == b2:
            return False
        
        l12 = (abs(a1-a2)**2 + abs(b1-b2)**2)
        l13 = (abs(a1-a3)**2 + abs(b1-b3)**2)
        l23 = (abs(a3-a2)**2 + abs(b3-b2)**2)
        l = [l12,l13,l23]
        ls = sorted(l)
        
        if ls[0] + ls[1] == ls[2]:
            return True
        else:
            return False
    
    r1 = isRight(x1-1,y1,x2,y2,x3,y3)
    r2 = isRight(x1+1,y1,x2,y2,x3,y3)
    r3 = isRight(x1,y1-1,x2,y2,x3,y3)
    r4 = isRight(x1,y1+1,x2,y2,x3,y3)
    r5 = isRight(x1,y1,x2-1,y2,x3,y3)
    r6 = isRight(x1,y1,x2+1,y2,x3,y3)
    r7 = isRight(x1,y1,x2,y2-1,x3,y3)
    r8 = isRight(x1,y1,x2,y2+1,x3,y3)
    r9 = isRight(x1,y1,x2,y2,x3-1,y3)
    r10 = isRight(x1,y1,x2,y2,x3+1,y3)
    r11 = isRight(x1,y1,x2,y2,x3,y3-1)
    r12 = isRight(x1,y1,x2,y2,x3,y3+1)
    
    if isRight(x1,y1,x2,y2,x3,y3):
        print('RIGHT')
    elif r1 or r2 or r3 or r4 or r5 or r6 or r7 or r8 or r9 or r10 or r11 or r12:
        print('ALMOST')
    else:
        print('NEITHER')