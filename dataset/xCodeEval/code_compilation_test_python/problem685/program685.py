def program685():
    import sys
    
    n = int(sys.stdin.readline().strip())
    mas = map(int, sys.stdin.readline().strip().split())
    if len(mas) > 1:
        if mas[-1] - 1 == mas[-2]:
            print "UP"
        else:
            print "DOWN"
    elif mas[0]==15:
        print "DOWN"
    elif mas[0]==0:
        print "UP"
    elif:
        print "-1"