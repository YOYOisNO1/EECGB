def program3986():
    import sys
    
    x = int(sys.stdin.readline())
    
    if x % 2 == 1:
        x -= 1
        
    if x == 2:
        print 5
        sys.exit(0)
    
    for i in xrange(1,1111,2):
        can = i / 2 + 1
        can /= 2
        g = i / 2 - can
        can *= can
        can += g*g
        can *= 4   
        can += i / 4 * 2 * 2
        if can >= x:
            print i
            sys.exit(0)