def checkit(x1,y1,x2,y2):
        check = [[0 for i in range(8)]for j in range(8)]
        for i in range(1,9):
            if i%2 == 0:
                for j in range(1,9):
                    if j%2 == 0:
                        check[i-1][j-1] = 1
            else:
                for j in range(1,9):
                    if j%2!=0:
                        check[i-1][j-1] = 1
        if check[x1-1][y1-1] == check[x2-1][y2-1]:
            return True
        else:
            return False
        
def bishop_tell(x1,y1,x2,y2):
        bishop=0
        if not checkit(x1,y1,x2,y2):
            return 0
        else:
            if y1>y2:
                x1,x2 = x2,x1
                y1,y2 = y2,y1
                #print(x1,y1,x2,y2)
    
            if x2 > x1:
                #print('Bishop1')
                while x1<9 and y1<9:
                    x1+=1
                    y1+=1
                    if x1 == x2 and y1 == y2:
                        return 1
                        break
                
            if x1 > x2:
                #print('Bishop2')
                while x1>0 and y1<9:
                    x1-=1
                    y1+=1
                    #print(x1,y1)
                    if x1 == x2 and y1 == y2:
                        return 1
                        break 
                    
            
            return 2
    
    x1,y1,x2,y2 = map(int,input().split())
    
    rook = 0
    bishop = bishop_tell(x1,y1,x2,y2)
    king = 0
    
    # Calculate rook and king
    if x1 == x2 or y1 == y2:
        king = abs(x1-x2) + abs(y1-y2)
        rook = 1
    else:
        rook = 2
        steps = 0
        if y1>y2:
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        
        if x2>x1:
            while x1<9 and y1<9:
                x1+=1
                y1+=1
                steps+=1
                if x1==x2 or y1==y2:
                    break
            if x1 == x2 or y1 == y2:
                steps += abs(x1-x2) + abs(y1-y2)
        else:
            while x1>0 and y1<9:
                x1-=1
                y1+=1
                steps+=1
                if x1==x2 or y1==y2:
                    break
            if x1 == x2 or y1 == y2:
                steps += abs(x1-x2) + abs(y1-y2)
        king = steps
    print(rook,bishop,king)    