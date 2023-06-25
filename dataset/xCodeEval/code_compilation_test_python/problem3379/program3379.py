def program3379():
    a,x,y = map(int,(input().strip().split()))
    
    if(y<0 or y%a == 0):
        print(str(-1))
    elif x>a or x< (-1*a):
        print(str(-1))
    else:
        if(y>0 and y<a):
            if(x>(-1*a)/2 and x<a/2):
                print(str(1))
            else:
                print(str(-1))
        else:
            k = (y-a)//(2*a)
            yRem = (y-a) % (2*a)
    
            elif(yRem<a and yRem>0 and x>(-1*a)/2 and x<a/2):
                print(str(2 + 3*k))
            elif(yRem>a and yRem<2*a and x>0 and x<a):
                print(str(4+3*k))
            elif (yRem > a and yRem < 2 * a and x < 0 and x > (-1*a)):
                print(str(3+3*k))
            else:
                print(str(-1))