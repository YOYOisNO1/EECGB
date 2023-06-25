def program316():
    import math
    n = int( input())
    
    if n%2==0 :
        even = int(n/2) 
        odd = even
    else:
        even = int((n-1)/2) 
        odd = n-even
        
    res = even*(even+1) # n*(n+1)
    res -= odd*odd #n^2 
    
    print( res )