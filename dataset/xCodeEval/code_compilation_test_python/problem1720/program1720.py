def program1720():
    x,y,z=map(int,input().split())
    if (x-(y+z))*((x+z)-y)<0:
        print('?)
    else:
        if x-(y+z)>0:
            print('+')
        elif (x+z)-y<0:
            print('-')
        else:
            print('0')