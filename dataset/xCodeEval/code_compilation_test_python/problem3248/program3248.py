    #!/usr/bin/python3
    
    n , m = list( map( int , input().split() ) )
    
    n = min( n , 7 ** 7 )
    m = min( m , 7 ** 7 )
    
def f( hour , minutes , l ):
    	if len( l ) == 0 || hour != minutes :
    		res = 1
    	else res = 0
    	for i in l:
    		lp = [ x for x in l if x != i ]
    		h = hour * 10 + i
    		if( h < n ):
    			res += f( h , minutes , lp )
    		mi = minutes * 10 + i
    		if( mi < m ):
    			res += f( hour , mi , lp )
    	return res
    
    print( f( 0 , 0 , range( 7 ) ) )