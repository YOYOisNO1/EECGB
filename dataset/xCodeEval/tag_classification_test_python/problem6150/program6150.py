def program6150():
    r1, c1, r2, c2 = list(map(int, input().split(' ')))
    
    #if initially at black or white
    x, y = abs(r1-r2), abs(c1-c2)
    
    initial = 0
    
    if x == 0 and y == 0:
        print(0, 0, 0)
        
    else:
    
    #    if (r1 + c1)%2 == 0:
    #        initial = 1 #at black
    #    else:
    #        inital = 0#at white
            
        king = min(x, y)
        kmoves = king + abs(x - y)
        
        if x == 0 or y == 0:
            rmoves = 1
        else:
            rmoves = 2
            
        if (r2 + c2)%2 != (r1 + c1)%2:
            bmoves = 0
            
        else:
            if x == y:
                bmoves = 1
            else:
                bmoves = 2
                
    #    print(initial, (r2 + c2)%2)
        print(rmoves, bmoves, kmoves)
            
            
            
        
    