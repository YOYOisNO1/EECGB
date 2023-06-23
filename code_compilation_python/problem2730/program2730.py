def Y():
        x,y = x0,y0
        while x > 3:
            x -= 3
        while y > 3:
            y -=3
        y,x = x-1,y-1
        if now == 1:
            x,y = x,y
        if now == 2:
             x,y = x, y + 3
        if now == 3:
             x,y = x, y + 6
        if now == 4:
             x,y = x + 3, y
        if now == 5:
             x,y = x + 3, y + 3
        if now == 6:
             x,y = x + 3, y + 6
        if now == 7:
             x,y = x + 6, y
        if now == 8:
             x,y = x + 6, y + 3
        if now == 9:
             x,y = x + 6, y + 6
        return [x,y]
        
    
def coun(x1,x2,y1,y2):
        ans = 0
        for i in range(x1,x2 + 1):
            for j in range(y1,y2 + 1):
                if a[i][j] == '.':
                    ans += 1
        return ans
    
    
    
def F(xc,yc):
        x,y = xc,yc
        while x > 3:
            x -= 3
        while y > 3:
            y -=3
        y,x = x-1,y-1
        if x == 0 and y == 0:
            return 1
        if x == 0 and y == 1:
            return 4
        if x == 0 and y == 2:
            return 7
        if x == 1 and y == 0:
            return 2
        if x == 1 and y == 1:
            return 5
        if x == 1 and y == 2:
            return 8
        if x == 2 and y == 0:
            return 3
        if x == 2 and y == 1:
            return 6
        if x == 2 and y == 2:
            return 9
        
        
    a = []
    for i in range(11):
        b = input()
        if i != 3 and i != 7:
            a.append([b[0],b[1],b[2],b[4],b[5],b[6],b[8],b[9],b[10]])
    
    x0, y0 = map(int, input().split())
    
    now = F(x0,y0)
    
    if now == 1:
        kek = [0,2,0,2]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 2:
        kek = [0,2,3,5]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 3:
        kek = [0,2,6,8]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 4:
        kek = [3,5,0,2]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 5:
        kek = [3,5,3,5]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 6:
        kek = [3,5,6,8]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 7:
        kek = [6,8,0,2]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 8:
        kek = [6,8,3,5]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
    if now == 9:
        kek = [6,8,6,8]
        toch = coun(kek[0],kek[1],kek[2],kek[3])
        
    
    tow = Y()
    
    if toch == 0 or a[tow[0]][tow[1]] != '.':
        for i in range(9):
            for j in range(9):
                if a[i][j] == '.':
                    print('!',end ='')
                else:
                    print(a[i][j], end='')
                if j == 2 or j == 5 :
                    print(' ',end='')
            print()
            if i == 2 or i == 5:
                print()
    
            
    
    else:
        for i in range(9):
            for j in range(9):
                if a[i][j] == '.' and  i >= kek[0] and i <= kek[1] and j >= kek[2] and j <=kek[3] :
                    print('!',end ='')
                else:
                    print(a[i][j], end='')
                if j == 2 or j == 5 :
                    print(' ',end='')
            print()
            if i == 2 or i == 5:
                print()
        