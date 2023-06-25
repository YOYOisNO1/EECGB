def program2645():
    
    n, m, a, b = map(int, input().split()) 
    res = 100000000
    for x in range(0,1001) :
      for y in range(0,1001):
        if m*x + y >= n :
          res = min(res, b*x + y*a)
    print(res)