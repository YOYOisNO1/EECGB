def program1925():
    n,m=map(int,input().split())
    a=b=0
    while n>0 and m>0:
      if b=a: b+=3; a+=2; m-=1
      elif b<a: b+=3; m-=1
      else: a+=2; n-=1
    print(max(a+n*2,b+m*3))