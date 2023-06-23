def p(x):
      d=2
      while d*d<=x and x%d:
        d+=1
      return d*d>x
    n=input()
    print 1 if p(n) else 2 if 0==n%2 or p(n-2) else 3