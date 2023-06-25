def program842():
    x,y,z=list(map(int,input().split()))
    if z==0:
        if x>y:print('+')
        elif x<y:print('-')
        else:print(0)
    else:
        if x==y:
            print('?')
        elif x>y:
            if x>y+z and x+z>y:
                print('+')
            else:
                print('?')
        elif x<y:
            if y>x+z and y+z>x:
                print('-')
            else:
                print('?')