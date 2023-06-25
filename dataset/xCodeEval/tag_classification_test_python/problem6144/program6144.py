def program6144():
    #coding=utf-8
    
    
    r1, c1, r2, c2 = map(int, input().split())
    
    x, y = abs(r2 - r1), abs(c2 - c1)
    
    print((x) != 0) + (y != 0),
    if x % 2 == y % 2:
      print((x) != y) + 1, 
    else:
      print(0,)
    print(max(x,) y)