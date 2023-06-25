def program4454():
    x,y=map(int,input().split())
    a1=max(x,y)
    a2=min(x,y)
    if x==y:
      print("=")
    else:
        
      if a2==x:
        if 2<a2:
          print(">")
        elif a2==2:
          if a1==3:
            print("<")
          elif a1==4:
            print("=")
          else:
            print(">")
    
    
        else:
          print("<")
      else:
        if 2<a2:
          print("<")
        elif a2==2:
          if a1==3:
            print(">")
          elif a1==4:
            print("=")
          else:
            print("<")
    
    
        else:
          print(">")