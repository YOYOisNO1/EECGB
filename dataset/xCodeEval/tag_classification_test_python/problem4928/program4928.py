    
def fckset( arr , i , ans , m , s ):
        
        if i == len(arr):
            s.add( ans )
        else:
            fckset( arr , i+1 , ( ans+arr[i] )%m , m , s  )
            fckset( arr , i+1 , ans , m , s  )
    
            
    
    n, m = map( int , input().split(" ") )
    arr = list( map( int , input().split(" ") ) )
    
    x = set()
    y = set()
    h1 = fckset( arr[:n//2] , 0 , 0 , m , x )
    h2 = fckset( arr[n//2:] , 0 , 0 , m , y )
    
    # h1.sort()
    
    x = list(x)
    y = list(y)
    
    y.sort()
    
        
    import bisect
    
    print(max(i+y[bisect.bisect_left(y,m-i)-1]for i in x))
        