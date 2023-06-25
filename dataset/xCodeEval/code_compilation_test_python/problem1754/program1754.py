def program1754():
    b = [['.' for c in range(10)] for y in range(10)]
    
    for x in range (10):
        tmp = input()
        for y in range(10):
            b[x][y] = tmp[y]
            if b[x][y] == '.':
                b[x][y] = 'c'
    
    for x in range(10):
        for y in range(6):
            tmp = 0
            check= False
            if b[x][y] == 'X':
                for c in range(5):
                    if b[x][y+c] in "Xc":
                        if b[x][y+c] == 'c':
                            if(check):
                                tmp = 0
                                break
                            check = True
                        tmp+=1
                if tmp == 5:
                    print("YES")
                    exit()
    for y in range(10):
        for x in range(6):
            tmp = 0
            check= False
            if b[x][y] == 'X':
                for c in range(5):
                    if b[x+c][y] in "Xc":
                        if b[x+c][y] in 'c':
                            if(check):
                                tmp = 0
                                break
                            check = True
                        tmp+=1
                if tmp == 5:
                    print("YES")
                    exit()
    
    for y in range(6):
        for x in range(6):
            tmp = 0
            check= False
            if b[x][y] == 'X':
                for c in range(5):
                    if b[x+c][y+c] in "Xc":
                        if b[x+c][y+c] in 'c':
                            if(check):
                                tmp = 0
                                break
                            check = True
                        tmp+=1
                if tmp == 5:
                    print("YES")
                    exit()
    
    for y in xrange(4,10):
        for x in range(6):
            tmp = 0
            check= False
            if b[x][y] == 'X':
                for c in range(5):
                    if b[x+c][y-c] in "Xc":
                        if b[x+c][y-c] in 'c':
                            if(check):
                                tmp = 0
                                break
                            check = True
                        tmp+=1
                    
                if tmp == 5:
                    print("YES")
                    exit()
    
    
    print("NO")