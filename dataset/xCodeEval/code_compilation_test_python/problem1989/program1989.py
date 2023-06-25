def program1989():
    
    
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    
    a = (x1 - x2)**2 + (y2 - y1)**2
    
    b = (x1 - x3)**2 + (y3 - y1)**2
    
    c = (x2 - x3)**2 + (y3 - y2)**2
    
    a,b,c = sorted([a,b,c])
    temp = 0
    if abs(a + b - c) < 0.1:
        temp = 1
        print('RIGHT')
    
    if temp == 0:
     x1+=1
     a = (x1 - x2)**2 + (y2 - y1)**2
    
     b = (x1 - x3)**2 + (y3 - y1)**2
    
     c = (x2 - x3)**2 + (y3 - y2)**2
    
     a,b,c = sorted([a,b,c])
     if abs(a + b - c) < 0.1:
        temp = 1
        print('ALMOST')
    
    if temp == 0:
     y1+=1
     a = (x1 - x2)**2 + (y2 - y1)**2
    
     b = (x1 - x3)**2 + (y3 - y1)**2
    
     c = (x2 - x3)**2 + (y3 - y2)**2
    
     a,b,c = sorted([a,b,c])
    
     if abs(a + b - c) < 0.1:
        temp = 1
        print('ALMOST')
    
    if temp == 0:
     x2+=1
     a = (x1 - x2)**2 + (y2 - y1)**2
    
     b = (x1 - x3)**2 + (y3 - y1)**2
    
     c = (x2 - x3)**2 + (y3 - y2)**2
    
     a,b,c = sorted([a,b,c])
     if abs(a + b - c) < 0.1:
        temp = 1
        print('ALMOST')
    
    if temp == 0:
     y2+=1
     a = (x1 - x2)**2 + (y2 - y1)**2
    
     b = (x1 - x3)**2 + (y3 - y1)**2
    
     c = (x2 - x3)**2 + (y3 - y2)**2
    
     a,b,c = sorted([a,b,c])
    
     if abs(a + b - c) < 0.1:
        temp = 1
        print('ALMOST')
    
    
    if temp == 0:
     x3+=1
     a = (x1 - x2)**2 + (y2 - y1)**2
    
     b = (x1 - x3)**2 + (y3 - y1)**2
    
     c = (x2 - x3)**2 + (y3 - y2)**2
    
     a,b,c = sorted([a,b,c])
     if abs(a + b - c) < 0.1:
        temp = 1
        print('ALMOST')
    
    if temp == 0:
     y3+=1
     a = (x1 - x2)**2 + (y2 - y1)**2
    
     b = (x1 - x3)**2 + (y3 - y1)**2
    
     c = (x2 - x3)**2 + (y3 - y2)**2
    
     a,b,c = sorted([a,b,c])
    
     if abs(a + b - c) < 0.1:
        temp = 1
        print('ALMOST')
    
    if temp == 0:
        print('NEIT