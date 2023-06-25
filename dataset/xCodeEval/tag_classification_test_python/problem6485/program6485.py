def program6485():
    a,b,x1,y1,x2,y2 = map(int,input().split())
    
    a1 = x1+y1
    a2 = x2+y2
    
    b1 = x1-y1
    b2 = x2-y2
    
    ad = a2//(2*a) - a1//(2*a)
    bd = b2//(2*b) - b1//(2*b)
    
    print(max(abs(ad),abs(bd)))