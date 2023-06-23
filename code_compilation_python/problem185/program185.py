def program185():
    x,y = map(int,input().split())
    me = y-1
    if(y == 0):
        print "No"
    elif(x < me):
        print "No"
    else:
        left = x-me
        if(left == 0):
            print "Yes"
        else:
            if(left%2 == 0):
                print "Yes"
            else:
                print "No"