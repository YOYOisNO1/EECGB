def is_prime( n ):
    
        i = 2
    
        while i * i <= n:
    
            if n % i == 0:
                return ( False )
    
            i += 1
    
        return ( True )
    
    m = {}
    
    p = []
    
    i = 2
    
    while len(p) < 12:
    
        if is_prime(i):
            p.append(i)
    
        i += 1
    
    INF = 10**18
    
    m = {}
    
    ans = INF
    
def f( a, b, div ):
    
        global ans
    
        if b >= len(p):
            return
    
        if div == n:
            ans = min( ans, a )
            return
    
        for j in range( 1, 60 ):
            if a <= ans//p[b]:
                a *= p[b]
                f( a, b+1, div*(j+1) )
            else:
                break
    
    n = int( input() )
    
    #for i in range( len(p) ):
    #    f( p[i], i )
    f( 1, 0, 1 )
    
    print( ans )