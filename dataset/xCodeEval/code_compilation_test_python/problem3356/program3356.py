def program3356():
    p, y = map(int, input().split())
    
    l = []
    ans = -1
    for i in range(2, p+1):
      x = 1
      while i*x <= y:
        if i*x not in l:
          l.append(i*x)
        x += 1
    for i in range(y, 1,-1):
      if i not in l:
        ans = i
        break
    print(ans)
      