    p = (0, 0)
    v = {p}
    
    
def left():
        return (p[0] - 1, p[1])
    
def right():
        return (p[0] + 1, p[1])
    
def up():
        return (p[0], p[1] + 1)
    
def down():
        return (p[0], p[1] - 1)
    
    
    for x in input():
        if x == 'L':
            p = left()
            s = {p, left(), up(), down()}
        elif x == 'R':
            p = right()
            s = {p, right(), up(), down()}
        elif x == 'U':
            p = up()
            s = {p, left(), right(), up()}
        elif x == 'D':
            p = down()
            s = {p, left(), right(), down()}
        
        if any(x in v for x in s):
            print("BUG")
            break
        
        v.add(p)
    else:
        print("OK")