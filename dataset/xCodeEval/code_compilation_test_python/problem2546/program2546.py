    from sys import stdin,stdout
    import math
    
def gcd_ext(a, b):
        if b == 0:
            return (a,1,0)
        else:
            g,x,y = gcd_ext(b, a%b)
            t = x;
            x = y;
            y = t - a/b*y
            return g,x,y
    
    a1,b1,a2,b2,L,R = [ int(x) for x in stdin.readline().rstrip().split() ]
    
    A = a1
    B = a2
    C = b2 - b1
    
    G,X,Y = gcd_ext( A, B )
    
    if C % G != 0:
        print 0
        sys.exit(0)
    
    X = X*C/G
    Y = Y*C/G
    
    K = max( [ math.ceil( -X*G/float(B) ), math.ceil( Y*G/float(A) ) ] )
    
    #print int(K)
    
    #print "LOWER", (L - b1 - a1 * X) * G / float( B * a1 ), (L - b2 + a2 * Y) * G / float( A * a2 )
    #print "UPPER", (R - b1 - a1 * X) * G / float( B * a1 ), (R - b2 + a2 * Y) * G / float( A * a2 )
    #print "S", a1 * (X + B*K/G) + b1, "T", a2 * (-Y + A*K/G) + b2
    
    K = max( [ K, math.ceil( (L - b1 - a1 * X) * G / float( B * a1 ) ) ] )
    
    ANS = math.floor( (R - b1 - a1 * X) * G / float( B * a1 ) ) - K + 1
    
    print max( [ 0, int(ANS) ] )