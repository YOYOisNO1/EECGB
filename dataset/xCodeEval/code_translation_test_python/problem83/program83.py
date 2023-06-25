def program83():
    n, bx = map(int, input().split())
    x = map(int, input().split())
    m, by = map(int, input().split())
    y = map(int, input().split())
    
    numx = 0
    for e, v in enumerate(reversed(x)):
        numx += v*(bx**e)
    numy = 0
    for e, v in enumerate(reversed(y)):
        numy += v*(by**e)
    
    if numx < numy:
        print('<')
    elif numx > numy:
        print('>')
    else:
        print('=')
    
    