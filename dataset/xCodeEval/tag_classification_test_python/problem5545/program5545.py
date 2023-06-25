def program5545():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    
    res = 0
    
    if(a <= (b-c)):
      res = n/a
    else:
      aux = (n-c)/(b-c)
      #print(aux)
      if(aux >= 0):
    	  res = aux
    	  n = n-b*aux+c*aux
      #print(n)
      if(n >= a):
        aux2 = n/a
        res+= aux2
      
    print(res)