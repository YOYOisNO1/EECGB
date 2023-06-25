def program3674():
    x,y = map(int,input().split())
    ans = 4*max(abs(x),abs(y)) - 2
    if abs(x) > 1 or abs(y) > 1:
        if abs(x) > abs(y):
            if x > 0:
                if x == 1 - y:
                    print(ans) -2
                else:
                    print(ans) - 1
            else:
                print(ans) + 1
        elif abs(x) < abs(y):
            if y > 0:
                print(ans) 
            else:
                print(ans) + 2
        else:
            if x > 0 and y > 0:
                print(ans) - 1
            elif x < 0 and  y > 0:
                print(ans)
            elif x < 0 and y < 0:
                print(ans) + 1
            else:
                print(ans) + 2
    else:
        if x == 0 and y == 0:
            print(0)
        elif x == 1 and y == 0:
            print(0)
        elif x == 1 and  y == 1:
            print(1)
        elif x == 0 and  y== 1:
            print(2)
        elif x == -1 and y == 1:
            print(2)
        elif x == -1 and y == 0:
            print(3)
        elif x == -1 and y == -1:
            print(3)
        elif x == 0 and y == -1:
            print(4)
        elif x == 1 and y == -1:
            print(4)