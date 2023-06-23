def dfs(grid, x, y):
        if [x, y] == [0, 0]:
            toggle(x+1,y)
            toggle(x,y+1)
        
        if [x, y] == [0, 1]:
            toggle(x,y-1)
            toggle(x+1,y)
            toggle(x,y+1)
    
        if [x, y] == [0, 2]:
            toggle(x,y-1)
            toggle(x+1,y)
    
        if [x, y] == [1, 0]:
            toggle(x-1,y)
            toggle(x+1, y)
            toggle(x, y+1)
    
        if [x, y] == [1, 1]:
            toggle(x-1, y)
            toggle(x, y-1)
            toggle(x+1, y)
            grid[x][y+1] = toggle(x, y+1)
    
        if [x, y] == [1, 2]:
            toggle(x-1, y)
            toggle(x, y-1)
            toggle(x+1, y)
    
        if [x, y] == [2, 0]:
            toggle(x-1 , y)
            toggle(x, y+1)
    
        if [x, y] == [2, 1]:
            toggle(x-1, y)
            toggle(x, y-1)
            toggle(x, y+1)
    
        if [x, y] == [2, 2]:
            toggle(x-1 , y)
            toggle(x , y-1)
    
        toggle(x, y)
    
    
def toggle(x, y):
        if result[x][y] == 1:
            result[x][y] = 0
        else:
            result[x][y] = 1
    
    
    grid = []
    result = []
    for i in range(3):
        grid.append([int(x) for x in input().split()])
        result.append([1 for x in range(3)])
    
    
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                continue
            
            val = grid[row][col]
            if val % 2 == 0:
                continue
            else:
                dfs(grid, row, col)
    
    
    
    for row in range(3):
        for col in range(3):
            print(result[row][col)
        print()
    