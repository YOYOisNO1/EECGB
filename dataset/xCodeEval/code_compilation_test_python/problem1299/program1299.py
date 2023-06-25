def program1299():
    #coding:utf-8
    #! usr/bin/env python
    nxy=input()
    n=int(nxy.split(' ')[0]
    x=int(nxy.split(' ')[1]
    y=int(nxy.split(' ')[2]
    
    if real(x)/n>y:
        print 0
    elif y>=100:
        print int((y*n-100*x)/(100-y)+1)
    else:
        print int((y*n-100*x)/(y-100)+1)