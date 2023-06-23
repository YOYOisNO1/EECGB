def program4341():
    import math
    
    n, m = map(int, input().split())
    x = int(input()) - 1
    
    a = n - (x*2)
    b = m - (x*2)
    
    if a > 0 and b > 0:
        if a == b == 1:
            print 1
        else:
            if a == 1:
                print int(math.ceil(b/2))
            elif b == 1:
                print int(math.ceil(a/2))
            else: print (2*a + 2*(b-2))/2
    else:
        print 0