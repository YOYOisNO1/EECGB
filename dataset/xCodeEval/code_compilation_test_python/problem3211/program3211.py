def ok( s, r ):
      res = s // 50 % 475
      for i in range( 25 ):
        res = ( res * 96 + 42 ) % 475
        if 26 + res == r:
          return True
      return False
    
    P, X, Y = map( int, input().split() )
    
    if any( ok( i, P ) for i in range( X, Y - 1, -50 ) ):
      exit( print( 0 ) )
    else:
      ans = 1
      X += 100
      while True:
        if ok( X, P ) or ok( X - 50, P ):
          exit( print( ans ) )
      X += 100
      ans += 1
    