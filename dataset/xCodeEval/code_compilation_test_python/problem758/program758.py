def program758():
    from math import sqrt
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    if (abs(y2-y1)**2+abs(x2-x1)**2==abs(y3-y2)**2+abs(x3-x2)**2 and (y1-y2)*(x1-x3)!=(x1-x2)*(y1-y3):
        print "Yes"
    else:
        print "No"