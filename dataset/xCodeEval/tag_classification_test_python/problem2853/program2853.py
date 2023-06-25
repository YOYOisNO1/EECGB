def program2853():
    x = input()
    y = input()
    print( -1 if any( ord( x[ i ] ) < ord( y[ i ] ) for i in range( len( x ) ) ) else y )