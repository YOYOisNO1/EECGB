    #!/usr/bin/env python
    
    import sys
    
    n, m, x, y, a, b = map(int,sys.stdin.readline().split())
    
    #simplify a i b
    #----
def blya(num):
        if num==int(num):
            return num
        #if int(num)==0:
        #    return 1
        return int(min(str(int(num)),str(int(num)+1)))
        
    a2, b2 = a, b
    while a2!=0 and b2!=0:
        if a2 > b2:
            a2 = a2 % b2
        else:
            b2 = b2 % a2
     
    a /= a2+b2
    b /= a2+b2
    
    
    k = min(n/a, m/b)
    w = k*a
    h = k*b
    
    x1 = x-float(w)/2
    x2 = x+float(w)/2
    y1 = y-float(h)/2
    y2 = y+float(h)/2
    
    if x1<0 or x2>n:
        if x1<0:
            x1 = 0
            x2 = x1 + w
        else:
            x2 = n
            x1 = x2 - w
    else:
        if int(x1)!=x1:
            x1 = blya(x1)
            x2 = x1 + w
    
    if y1<0 or y2>m:
        if y1<0:
            y1 = 0
            y2 = y1 + h
        else:
            y2 = m
            y1 = y2 - h
    else:
        if int(y1)!=y1:
            y1 = blya(y1)
            y2 = y1 + h
    
    print(int(x1)) ,int(y1), int(x2), int(y2)
    
    #print(n,m,x,y,a,b)