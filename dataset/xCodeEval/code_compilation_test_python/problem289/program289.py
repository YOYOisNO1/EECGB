def program289():
    n = int(input())
    
    currentPos = 0
    north = True
    south = False
    
    for x in range(n):
        dist, d = input().split()
        dist = int(dist)%40000
        if north and d != 'South':
            print ('NO')
            break
        elif south and d!= 'North':
            print ('NO')
            break
        elif d in ('West', 'East'):continue
        while dist>0:
            if d == 'North':
                steps = min(dist,currentPos)
                currentPos -= steps
                dist -= steps
                d = 'South'
            elif d == 'South':
                steps = min(dist,20000-currentPos)
                currentPos += steps
                dist -= steps
                d = 'South'
    
        north = currentPos == 0
        south = currentPos == 20000
    
    else:
        print (('NO','YES')[currentPos == 0])