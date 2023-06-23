def program4482():
    from collections import defaultdict
    
    N, K, S = map( int, input().split() )
    A = list( map( int, input().split() ) )
    
    fact = [ 1 ]
    for i in range( 1, 20, 1 ):
      fact.append( fact[ i - 1 ] * i )
    
    ldp = [ [ defaultdict( int ) for i in range( 1 << N // 2 ) ] for j in range( K + 1 ) ]
    ldp[ 0 ][ 0 ][ 0 ] = 1
    for i in range( K + 1 ):
      for s in range( 1 << N // 2 ):
        for j in range( N // 2 ):
          if ~s >> j & 1:
            for key in ldp[ i ][ s ]:
              ldp[ i ][ s | 1 << j ][ key + A[ j ] ] += ldp[ i ][ s ][ key ]
              if i + 1 <= K and A[ j ] <= 18:
                ldp[ i + 1 ][ s | 1 << j ][ key + fact[ A[ j ] ] ] += ldp[ i ][ s ][ key ]
    
    lbag = [ defaultdict( int ) for i in range( K + 1 ) ]
    for i in range( K + 1 ):
      for j in range( 1 << N // 2 ):
        for key in ldp[ i ][ j ]:
          lbag[ i ][ key ] += ldp[ i ][ j ][ key ]
    
    rdp = [ [ defaultdict( int ) for i in range( 1 << N - N // 2 ) ] for j in range( K + 1 ) ]
    rdp[ 0 ][ 0 ][ 0 ] = 1
    for i in range( K + 1 ):
      for s in range( 1 << N - N // 2 ):
        for j in range( N - N // 2 ):
          if ~s >> j & 1:
            for key in rdp[ i ][ s ]:
              rdp[ i ][ s | 1 << j ][ key + A[ N // 2 + j ] ] += rdp[ i ][ s ][ key ]
              if i + 1 <= K and A[ N // 2 + j ] <= 18:
                rdp[ i + 1 ][ s | 1 << j ][ key + fact[ A[ N // 2 + j ] ] ] += rdp[ i ][ s ][ key ]
    
    ans = 0
    for i in range( K + 1 ):
      for s in range( 1 << N - N // 2 ):
        for key in rdp[ i ][ s ]:
          for j in range( 0, K - i + 1, 1 ):
            ans += lbag[ j ][ S - key ]
    
    print( ans )