    GI = lambda: int(input()); GIS = lambda: map(int, input().split()); LGIS = lambda: list(GIS())
    
def main():
      n, d = GIS()
      ps = LGIS()
      ps.sort()
    
      m = {}
  def recurse(l, r):
        if (l, r) in m:
          return m[(l, r)]
        if ps[r] - ps[l] <= d:
          return 0
        res = 1 + min(recurse(l+1, r), recurse(l, r-1))
        m[(l, r)] = res
        return res
    
      print(recurse(0, n-1))
    
    main()