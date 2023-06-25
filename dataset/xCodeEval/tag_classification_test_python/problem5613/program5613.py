    import sys
    
def doit( nm ):
      mn=min(nm)
      mx=max(nm)
      prod = mx*mn
      if mn<2: return prod
      if mn==2:
        if mx<4: return [None,None,4,4][mx]
        return mx + doit((2,mx%4)) - (mx%4)
      return (prod+1)/2
    
    print( doit( map(int, sys.stdin.readline().strip('\n\r ').split()[:2]) ) )