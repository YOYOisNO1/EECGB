def program840():
    x,y,z = input().split()
    x=int(x)
    y=int(y)
    z=int(z)
    result = '0'
    if(z==0):
        if (x>y):
            result='+'
        elif (y>x):
            result='-'
        else:
            result='0'
    else:
        if(x>y+z):
            result='+'
        elif(y>x+z):
            result='-'
        else:
            result='?'
    
    
    print((result))