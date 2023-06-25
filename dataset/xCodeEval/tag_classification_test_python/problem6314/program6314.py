def program6314():
    a,b = map(int,input().split())
    if a==b:
      print(1)
    else:
      ans = 1
      a += 1
      while a <= b:
        ans *= a
        a += 1
        if ans%10==0:
          break
      print(ans%10)