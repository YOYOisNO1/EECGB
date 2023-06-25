def program843():
    x,y,z=list(map(int,input().split()))
    if x==y and z==0:
        print(0)
    elif x==y and z>1:
        print('?')
    elif x>y and z==0:
        print('+')
    elif x<y and z==0:
        print('-')
    elif x>0 and y==0 and z<x:
        print('+')
    elif x>0 and y==0 and z>=x:
        print('?')
    elif y>0 and x==0 and z<y:
        print('-')
    elif y>0 and x==0 and z>=y:
        print('?')
    else:
        if x+z<y:
            print('-')
        elif y+z<x:
            print('+')
            
        else:
            print('?')