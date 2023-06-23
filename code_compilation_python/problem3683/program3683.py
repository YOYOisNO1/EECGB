def program3683():
    n, b = map(int, input().split())
    x = map(int, input().split())
    X = 0
    for i in x:
        X = X * b + i
    n, b = map(int, input().split())
    y = map(int, input().split())
    Y = 0
    for i in y:
        Y = Y * b + i:
    
    if X == Y:
        print "="
    elif X > Y:
        print ">"
    else:
        print "<"