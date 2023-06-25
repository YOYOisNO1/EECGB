def program1717():
    d = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    
    if(a == 1000000000000000000):
      qntd = 999999999999999995
    else if(a <= (b - c)):
      qntd = d / a
    else :
      if(d >= b):
        qntd = (d - c) / (b - c)
      else :
        qntd = 0
    
    print (qntd)