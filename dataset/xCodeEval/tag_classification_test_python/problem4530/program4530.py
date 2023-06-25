def program4530():
    import sys
    
    a, b, m, x = tuple(map(int, input().split()))
    z=[0]*(m+1)
    cnt=1
    z[x]=cnt
    while True:
      cnt += 1
      x = (x*a+b)%m
      if z[x] > 0:
        print(str(cnt-z[x]))
        sys.exit(0)
      z[x] = cnt