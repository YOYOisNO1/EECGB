def program1357():
    a=int(input())
    b=int(input())
    c=int(input())
    k=1
    for j in range (0,5,1):
      if k==1: 
        w=a+(b*c)
        k=k+1
      else:
        if k==2:
          j=a*(b+c)
          k=k+1
          h=(a+b)*c
          if j<=h:
            x=h
          else:
            x=j
        else:
          if k==3:
            y=(a*b)+c
            k=k+1
          else:
            if k==4:
              z=a*b*c
              k=k+1
            else:
              if k==5:
               l=a+b+c
    if l>w:
      if l>x:
        if l>y:
          if l>z:
            print(l)
          else:
            print(z)
        else:
          if y>z:
            print(y)
          else:
            print(z)
      else:
        if x>y:
          if x>z:
            print(x)
          else:
            print(z)
        else:
          if y>z:
            print(y)
          else:
            print(z)
    else:
      if w>x:
        if w>y:
          if w>z:
            print(w)
          else:
            print(z)
        else:
          if y>z:
            print(y)
          else:
            print(z)
      else:
        if x>y:
          if x>z:
            print(x)
          else:
            print(z)
        else:
          if y>z:
            print(y)
          else:
            print(z)
          