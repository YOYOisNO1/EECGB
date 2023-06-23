def program2138():
    x1,y1=[int(i) for i in input().split()]
    x2,y2=[int(i) for i in input().split()]
    x3,y3=[int(i) for i in input().split()]
    if((x1==x2 and x2==x3) or (y1==y2 and y2==y3)):
        print 1
    else if (x1==x2 or x1==x3 or x2==x3 or y1==y2 or y2==y3 or y1==y3):
        print 2
    else:
        print 3
        