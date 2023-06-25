    #Codeforces , Statues
    
    import sys
    from sys import stdin
    import copy
    
    ONLINE_JUDGE = 1
    
    if ONLINE_JUDGE == False:
        sys.stdin = open('input.txt', 'r')
    
    
def ok(x, y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False
    
    
    mat = [[x for x in input()] for i in range(8)]
    #print(type(mat))
    
    d = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, -1], [1,1], [-1, -1], [-1, 1]]
    bingo = False
    while True:
        tmp = copy.deepcopy(mat)
        for i in range(8):
            for j in range(8):
                if 'M' == tmp[i][j]:
                    for k in range(8):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if ok(x, y) and mat[x][y] != 'S':
                            mat[x][y] = 'M'
    
        if('M' == mat[0][7]):
            bingo = True
            break
    ##    for i in range(8):
    ##        print(mat[i])
    ##    print(for) i in range(7, -1, -1):
            for j in range(8):
                if 'S' == mat[i][j]:
                    if i + 1 < 8:
                        mat[i + 1][j] = 'S'
                    mat[i][j] = '.'
        cnt = 0
        for i in range(8):
            for j in range(8):
                if mat[i][j] == 'M':
                    cnt += 1
    
        if 0 == cnt:
            break
    if bingo:
        print('WIN')
    else:
        print('LOSE')
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    
        
    