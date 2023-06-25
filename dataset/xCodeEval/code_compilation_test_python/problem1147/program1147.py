def program1147():
    k,a,b,v=map(int,input().split())
    n=(a+v-1)/v
    d=b/(k-1)*k
    if d<n:
      n-=d
      x=b/(k-1)
      b%=k-1
      if b+1<n:
        n-=b+1
        x+=1
      print x+n
    else:
      print (n+k-1)/k
    k,a,b,v=map(int,input().split())
    n=(a+v-1)/v
    d=b/(k-1)*k
    if d<n:
      n-=d
      x=b/(k-1)
      b%=k-1
      if b+1<n:
        n-=b+1
        x+=1
      print x+n
    else:
      print (n+k-1)/k