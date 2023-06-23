def program3793():
    [n,m,a,b] = [int(x) for x in input().split()]
    
    if (a-1)%m == 0:
        if b - a < m:
            print 1
        elif b%m == 0:
            print 1
        elif b == n:
            print 1
        else:
            print 2
    else:
        if (a-1)/m*m+m >= b:
            print 1
        elif (a-1)/m*m+2*m >= b:
            print 2
        elif b%m == 0:
            print 2
        elif b == n:
            print 2
        elif (b-a+1)%m == 0:
    	print 2
        else:
            print 3
            
        