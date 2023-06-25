def program298():
    clockwise = ['^', '>', 'v', '<']
    counterclockwise = ['^', '<', 'v', '>']
    
    start , end = input().split()
    n = int(input())
    
    n = n % 4
    
    x = clockwise.index(end) - clockwise.index(start)
    y = counterclockwise.index(end) - counterclockwise.index(start)
    
    if x<0:
        x += 4
    if y<0:
        y += 4
    
    if x == y:
        print("undefined")
    elif x == n:
        print("cw")
    else:
        print("ccw")
    
    