def program4899():
    n,p,w,d = map(int, input().split())
    
    x, y = -1, -1
    for y in range(w):
      if y*d > p:
        continue
    
      if (p - y*d) % w == 0:
        x = (p-y*d) // w
        if x + y <= n:
          print((x,) y, n-x-y)
          break
    else:
      print(-1)
    
    
    