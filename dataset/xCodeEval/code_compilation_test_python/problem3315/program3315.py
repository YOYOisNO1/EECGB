def program3315():
    d, L, v1, v2  = map( int, input().split() )
    
    f1, f2 = 0, L
    ans = 0
    
    while True:
    	next1 = f1+v1
    	next2 =  f2-v2
    	if abs( next1 - next2 ) < d or next1 >= next2 + d:
    		break
    	f1 += v1
    	f2 -= v2
    	#print f1,f2
    	ans += 1
    #print f1, f2	
    if v1 != v2:
    	ans += abs( ( 2*d  - f1 -f2 ) / ( v1  + v2 + 0.0) )-1
    	
    print "%f" % ( max( 1,ans ) )