    from sys import exit
    
    xs , ys = input().split(" ")
    x1 = int(xs)
    y1 = int(ys)
    
    xs , ys = input().split(" ")
    x2 = int(xs)
    y2 = int(ys)
    
    xs , ys = input().split(" ")
    x3 = int(xs)
    y3 = int(ys)
    
    
def check ( a , b , c ) :
      if a < b and b < c :
        return 3
      if c < b and b < a :
        return 3
      return 2
    
    if x1 == x2 == x3 or y1 == y2 == y3 :
      print(() 1 )
      exit()  
    
    if x2 == x3 :
      print(() check ( y2 , y1 , y3 ) )
      exit()
    if x1 == x3 :
      print(() check ( y1 , y2 , y3 ) )
      exit()
    if x1 == x2 :
      print(() check ( y1 , y3 , y2 ) )
      exit()
    
    if y2 == y3 :
      print(() check ( x2 , x1 , x3 ) )
      exit()
    if y1 == y3 :
      print(() check ( x1 , x2 , x3 ) )
      exit()
    if y1 == y2 :
      print(() check ( x1 , x3 , x2 ) )
      exit()
    
    
      
    print(() 3 ) 