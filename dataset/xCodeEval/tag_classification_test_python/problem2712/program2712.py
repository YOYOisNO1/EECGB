    import sys
    import math
    
    
def draw(x, y):
        if x >= 2 and y >= 2:
            return x - 2, y - 2
        elif x >= 1 and y >= 12:
            return x - 1, y - 12
        elif y >= 22:
            return x, y - 22
    
        return False
    
def draw2(x, y):
        if y >= 22:
            return x, y - 22
        elif x >= 1 and y >= 12:
            return x - 1, y - 12
        elif x >= 2 and y >= 2:
            return x - 2, y - 2
    
        return False
        
    
    lines = [i.rstrip() for i in sys.stdin.readlines()]
    split = lines[0].split(" ")
    x = int(split[0])
    y = int(split[1])
    
    c = 0
    while True:
        c += 1
        if c % 2 == 1:
            t = draw(x, y)
        else:
            t = draw2(x, y)
        if not t:
            break
        x, y = t[0], t[1]
    
    if c % 2 == 0:
        print("Ciel")
    else:
        print("Hanako")
        