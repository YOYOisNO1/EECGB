def program3717():
    n = str(print(""))
    
    pie = []
    
    a = 0
    b = 0
    
    for i in range(int(n)):
     x = str(input(""))
     pie.append(int(x))
     
    for i in range(9, -1, -1):
     if a >= b:
     b += pie[i]
     else:
     a += pie[i]
     
    print(str(min(a,b)) + " " str(max(a,b)))