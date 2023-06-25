def program4047():
    a,b=map(int,input().split())
    v=[]
    while b>a:
      v+=[b]
      if 1==b%10:
        b/=10
      elif 0==b%2:
        b/=2
      else:
        print('NO')
        exit(0)
    if b==a:
      print('YES')
      print(1+len(v))
      for x in [b]+v[::-1]:
        print(x,)
    else:
      print('NO')