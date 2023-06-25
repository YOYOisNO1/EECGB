def program3487():
    import sys
    
    f = open('test.in','r')
    #f=sys.stdin
    x,y = map(int, f.readline().strip().split())
    
    if x>=2 and y>=24:
        x = x-y/12
        y %= 24
    
    while True:
        if 100*x+10*y>=220 and y>=2:
            #ceil
            if x>=2: x,y=x-2,y-2
            elif x==1: x,y=0,y-12
            else: y-=22
        else:
            print 'Hanako'
            break
        
        if 100*x+10*y>=220 and y>=2:
            #hanako
            if y>=22: y=y-22
            elif y>=12: x,y=x-1,y-12
            else: x,y=x-2,y-2
        else:
            print 'Ceil'
            break
        