def program5756():
    import math
    import fractions
    x,y,n = map(float, input().split())
    if n >= y:
      grcd = fractions.gcd(int(x), int(y))
      print(str(int(x)/grcd)+"/"+str(int(y)/grcd))
    else:
      minx = miny = 1
      mini = 1.0
      for deno in range(int(n), 0, -1):
        nomi = math.floor(x * deno / y)
        if abs((x/y) - (nomi/deno)) <= abs((x/y) - ((nomi+1.0)/deno)):
          if abs((x/y) - (nomi/deno)) - mini < 2.2205e-16:
            mini = abs((x/y) - (nomi/deno))
            minx = int(nomi)
            miny = deno
        else:
          if abs((x/y) - ((nomi+1.0)/deno)) <= mini:
            mini = abs((x/y) - ((nomi+1.0)/deno))
            minx = int(nomi + 1.0)
            miny = deno
            
      print(str(minx)+"/"+str(miny))