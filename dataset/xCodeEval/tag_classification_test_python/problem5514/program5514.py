def program5514():
    a,x,y=map(int,input().split())
    if 0==y%a:
      print(-1)
    else:
      k=y/a
      w=1
      if k>1 and (0==k&0x01):
        w=2
      if x*2<=-a*w or x*2>=a*w:
        print(-1)
      else:
        if k<1:
          print(1)
        else:
          if k&0x01:
            print(k/2*3+2)
          else:
            if 0==x:
              print(-1)
            else:
              if x>0:
                print(k/2*3+1)
              else:
                print(k/2*3)