    import sys
    
def corner( a , b , s ) :
        res = 0
        if ( a > b ) :
            a , b = b , a
        if ( s > b ) :
            return a * b - corner( a , b , max( 0 , a + b - 1 - s ) )
        s1 = min( s , a )
        res = s1 * ( s1 + 1 ) / 2
        s2 = max( 0 , min( s - a , b - a ) )
        res += s2 * a
        return res
    
def cells( n , x , y , s ) :
        res = corner( x - 1 , y - 1 , s - 1 ) + corner( x - 1 , n - y , s - 1 )
        res += corner( n - x , y - 1 , s - 1 ) + corner( n - x , n - y , s - 1 )
        res += min( s , x - 1 ) + min( s , y - 1 ) + min( s , n - x ) + min( s , n - y )
        return res + 1  
    
def main() :
        n , x , y , c = [ int( x ) for x in sys.stdin.readline().split() ]
        if ( c <= 1 ) :
           print(0)
           return
        sHigh = 1
        while cells( n , x , y , sHigh ) < c :
            sHigh *= 2
        sLow = int( sHigh / 2 )
        while ( sHigh - sLow > 1 ) :
            sMid = ( sLow + sHigh ) / 2
            if ( cells( n , x , y , sMid ) >= c ) :
                sHigh = sMid
            else :
                sLow = sMid
        print(sHigh)
        return
    
    if __name__ == '__main__' :
        main()
        