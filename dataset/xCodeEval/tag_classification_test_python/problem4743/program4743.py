    n , m = map( int , input().split() )
    
    till = m+1;
    
    two = 2
    one = 1
    
def kotoase( x ):
        if x <= till : 
            return n;
        day = ( x - till );
        return ( n + day * m ) - ( (day * (day-one) ) >> one  ) - ( day * till );
    
    high = n;
    low = 1;
    mid = 0;
    Ans = n;
    
    while( low <= high ) :
        mid = (high + low) >> one;
        if kotoase( mid ) <= mid :
            Ans = mid;
            high = mid - one;
        else :
            low = mid + one;
    
    print( Ans )