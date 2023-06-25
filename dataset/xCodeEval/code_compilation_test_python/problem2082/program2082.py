def program2082():
    string = input()
    geo_map = [[0]*100 for i in range(100)]
    x = 50
    y = 50
    geo_map[x][y] = 1
    optimal_check = 0
    state = True
    for c in string:
        optimal_check = 0
        if c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        if geo_map[x][y] == 1:
            print('BUG')
            state = False
            break
        else:
            geo_map[x][y] = 1
    
        if geo_map[x+1][y] == 1:
            optimal_check += 1
        if geo_map[x-1][y] == 1:
            optimal_check += 1
        if geo_map[x][y+1] == 1:
            optimal_check += 1
        if geo_map[x][y-1] == 1:
            optimal_check += 1
        if optimal_check >= 2:
            print('BUG')
            state = False
            break
    
    
    if state:
        print('OK')
    
    
    
    