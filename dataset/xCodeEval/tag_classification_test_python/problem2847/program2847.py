    import sys
    
def main( ):
        n = int( sys.stdin.readline( ) )
        board = sys.stdin.readline( )
        for i in xrange( n ):
            for j in xrange( 1, n ):
                count = 0
                for k in xrange( 5 ):
                    count += ( i+j*k < n ) and board[ i+j*k ] == '*'
                if count == 5:
                    print("yes")
                    return
        print("no")
    
    main( )