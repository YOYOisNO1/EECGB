def inoneline(sol, move, final): 
        vec=(final[0]-sol[0], final[1]-sol[1])   
        cross=vec[1]*move[1]+vec[0]*move[0]
        if cross <= 0:
            return False
        veclen = vec[1]**2+vec[0]**2
        movlen = move[0]**2+move[1]**2
        if cross**2 != veclen*movlen:
            return False
        if veclen%movlen!=0:
            return False
        return True
        
    a, b = map(int, input('').split())
    movements=input('')
    steps={'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    px, py=0, 0
    posols=set([(px, py)])
    for movement in movements:
        x, y = steps[movement]
        px+=x
        py+=y
        posols.add((px, py))
        if (a, b) == (px, py):
            print 'YES'
            exit()
            
    if(px, py)==(0, 0):
        print 'NO'
        exit()
        
    for posol in posols:
        if inoneline(posol, (px, py),(a, b)):
            answer='Yes'  
            
    print answer