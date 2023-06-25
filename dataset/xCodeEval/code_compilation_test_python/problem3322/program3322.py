def program3322():
    x, y, m = map(int, input().strip().split(' '))
    
    if x <= 0 and y <= 0 and max(x,y) < m:
        return -1
    
    counter = 0
    while max(x,y) < m:
        if x < y:
            x = x + y
        else:
            y = x + y
        counter += 1
    
    print counter