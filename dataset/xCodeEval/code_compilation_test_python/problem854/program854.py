def program854():
    
    n,t = map(int,input().split())
    
    if t == 10:
    
      ans = int(t)*(10**(int(n)-2))
    
      if len(str(ans)) == int(n):
    
        print (ans)
    
      else:
    
        print('-1')
    
    else:  
    
      ans = int(t)*(10**(int(n)-1))
    
      if len(str(ans)) == int(n):
    
        print (ans)
    
      else:
    
        print('-1')
    
    