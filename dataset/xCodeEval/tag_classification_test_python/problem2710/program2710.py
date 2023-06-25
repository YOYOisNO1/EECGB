def c(x,y):
       if x*100+y*10 < 220:
           return 0
       if x>1 and y>1:
           return 1-h(x-2,y-2)
       if x>0 and y>11:
           return 1-h(x-1,y-12)
       if y>21:
           return 1-h(x,y-22)
       return 0
    
def h(x,y):
       if x*100+y*10 < 220:
           return 0
       if y>21:
           return 1-c(x,y-22)
       if x>0 and y>11:
           return 1-c(x-1,y-12)
       if x>1 and y>1:
           return 1-c(x-2,y-2)
       return 0
    
def o(x,y):
       g = 1
       while x*100+y*10>=220 and y>1:
         g=1-g
         if g==0:
           if x>1 and y>1:
             x=x-2
             y=y-2
             continue
           if x>0 and y>11:
             x=x-1
             y=y-12
             continue
           if y>21:
             y=y-22
             continue
         else:
           if y>21:
             y=y-22
             continue
           if x>0 and y>11:
             x=x-1
             y=y-12
             continue
           if x>1 and y>1:
             x=x-2
             y=y-2
             continue
       return 1-g
    
    #for x in range(30):
    #  for y in range(70):
    #    print(c(x,y)-o(x,y),)
    #  print(x,y=[int(i)) for i in input().split(' ')[:2]]
    if o(x,y)==1:
      print('Ciel')
    else:
      print('Hanako')
    