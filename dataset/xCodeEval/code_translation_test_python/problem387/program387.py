def program387():
    x1,y1 = map(int,input().split())
    
    x2,y2 = map(int,input().split())
    
    deltax = abs(x1-x2)
    deltay = abs(y1-y2)
    
    ayy = max(deltax,deltay)
    print(ayy)