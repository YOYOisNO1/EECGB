def program1297():
    #coding:utf-8
    #! usr/bin/env python
    n=input()
    x=input()
    y=input()
    
    if real(x)/n>y:
        print 0
    elif y>=100:
        print int((y*n-100*x)/(100-y)+1)
    else:
        print int((y*n-100*x)/(y-100)+1)