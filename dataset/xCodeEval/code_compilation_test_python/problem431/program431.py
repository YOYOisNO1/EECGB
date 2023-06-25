    
    
    '''s=[[0]*5]+[[0]+map(int,input().split())+[0] for _ in range(3)]+[[0]*5]
    for i in range(1,4):
        l=''
        for j in range(1,4):
            l+=str(1-(s[i][j]+s[i-1][j]+s[i+1][j]+s[i][j-1]+s[i][j+1])%2 )
        print l
    '''
    
        '''
    1 0 0
    0 0 0
    0 0 1
        '''
    
    g = [[0] * 5] + [[0] + map(int, input().split()) + [0] for i in range(3)] + [[0] * 5]
    
def f(x, y):
        return g[x][y - 1] + g[x][y] + g[x][y + 1] + g[x - 1][y] + g[x + 1][y]
    
    print '\n'.join([''.join([str(1 - f(x, y) % 2) for y in [1, 2, 3]]) for x in [1, 2, 3]])