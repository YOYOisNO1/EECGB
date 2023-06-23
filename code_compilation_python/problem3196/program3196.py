def  bad_sort ():
      n = int ( input () )
      if not (1 <= n <= 50): return -1
    
      if (n < 3): print -1
      else print " ".join( map ( str, range (n,0,-1)) )
    
    bad_sort ()