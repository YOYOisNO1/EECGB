def program1358():
    x = int(input())
    y = int(input())
    z = int(input())
    
    
    if(x == 1 and y != 1 and z != 1):
        print((x+y)*z)
    
    elif(z == 1 and x != 1 and y != 1):
        print((x*(y+z)))
    
    elif(y == 1 and (x <= z) and x != 1 and z != 1):
        print((x+y)*z)
    
    elif(y == 1 and (x > z)):
        print(x*(y+z))
    
    elif(x == 1 and y == 1 and z == 1):
        print(x+y+z)
    
    elif(x == 1 and y == 1 and z != 1):
        print((x+y)*z)
    
    elif(x == 1 and y != 1 and z == 1):
        print(x+y+z)
    
    elif(x != 1 and y == 1 and z == 1):
        print(x*(y+z))
    
    else:
        print(x*y*z)