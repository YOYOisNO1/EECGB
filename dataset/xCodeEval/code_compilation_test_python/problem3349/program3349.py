def program3349():
    x,y = map(int,input().split())
    #print(x,y)
    s = input()
    #print(s)
    pt = (0,0)
    path = [(0,0)]
    rect = [0,0,1,1]
    for c in s:
        if c == 'U': pt = (pt[0],pt[1]+1)
        elif c == 'D': pt = (pt[0],pt[1]-1)
        elif c == 'L': pt = (pt[0]-1,pt[1])
        elif c == 'R': pt = (pt[0]+1,pt[1])
    
        if pt[0] < rect[0]: rect[0] = pt[0]
        if pt[0] >= rect[2]: rect[2] = pt[0]+1
        if pt[1] < rect[1]: rect[1] = pt[1]
        if pt[1] >= rect[3]: rect[3] = pt[1]+1
        
        path.append(pt)
    
    #print(pt)
    #print(path)
    #print(rect)
    
    done = False
    if pt[0] == 0:
        if pt[1] == 0:
            if (x,y) in path:
                done = True
                print("Yes")
            else:
                print("No")
                done = True
        elif pt[1] > 0:
            n = max((y-rect[3])//pt[1]-2,0)
            while n*pt[1]+rect[1] <= y:
                if (x - n*pt[0],y - n*pt[1]) in path:
                    print("Yes")
                    done = True
                    break
                n += 1
        elif pt[1] < 0:
            n = max((y - rect[1])//pt[1]-2,0)
            while n*pt[1]+rect[3] >= y:
                if (x - n*pt[0],y-n*pt[1]) in path:
                    print("Yes")
                    done = True
                    break
    elif pt[0] > 0:
        n = max((x-rect[2])//pt[0]-2,0)
        while n*pt[0]+rect[0] <= x:
            if (x - n*pt[0],y - n*pt[1]) in path:
                print("Yes")
                done = True
                break
            n += 1
    elif pt[0] < 0:
        n = max((x-rect[0])//pt[0]-2,0)
        while n*pt[0]+rect[2] >= x:
            if (x - n*pt[0],y - n*pt[1]) in path:
                print("Yes")
                done = True
                break
            n += 1
    
    if not done:
        print("No")