def numOfClicks(i, j, clicks, rows, cols):
        positions = [[-1, 0], [0, -1], [0, 0] , [0, 1], [1, 0]]
        #               up  , left   , same   , right , down
        click = 0
        for pos in positions:
            if 0 <= i + pos[0] < rows and 0 <= j + pos[1] < cols:
                click += int(clicks[i + pos[0]][j + pos[1]])
    
        return click
    
    
    clicks = []
    
    for i in range(3):
        clicks.append(input().split())
    
    lights = [['1','1','1'],['1','1','1'],['1','1','1']]
    
    for i in range(len(clicks)):
        for j in range(len(clicks[0])):
            if numOfClicks(i, j, clicks, len(clicks), len(clicks[0])) % 2 == 0:
                lights[i][j] = '1'
            else:
                lights[i][j] = '0'
    
    for i in range(len(lights)):
        print("{0}".format("".join(lights[i])))