def program3909():
    w,m=map(int,input().split())
    c=0
    ok=1
    while m>0:  
      if (m%w+1+c)%w>2:
        ok=0
      c=(m%w+1+c)/w
      m/=w
    print('YES') if ok else 'NO'