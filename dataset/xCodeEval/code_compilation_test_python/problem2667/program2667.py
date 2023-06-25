def program2667():
    x,y = map(int,input().split())
    ans = 4*abs(x) - 2
    if abs(x) >= 1 and abs(y) >= 1:
        if abs(x) > abs(y):
            if x > 0:
                print ans -1
            else:
                print ans + 1
        elif abs(y) > abs(x):
            if y > 0:
                print ans 
            else:
                print ans + 2
        else:
            if x > 0:
                if x == y:
                    print ans - 1
                else:
                    print ans - 2
            else:
                if y > 0:
                    print ans
                else:
                    print ans + 1
    l = 0
    else:
        if x == 0 and y == 0:
            print 0
        elif x == 1 and y == 0:
            print 0
        elif x == 0 and y == 1:
            print 2
        elif x == -1 and y == 0:
            print 3
        elif x == 0 and y == -1 :
            print 4
        