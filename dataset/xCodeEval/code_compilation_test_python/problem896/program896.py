def program896():
    
    s = input()
    w = ""
    h = ""
    b = True
    s = list(s)
    for f in s:
      if not b:
        h += f
      if f != " " and b:
        w += f
      else:
        b = False
    n = int(w)
    a = int(h)
    
    
    n = int(input())
    a = int(input())
    
    if a % 2 == 0:
      tiempo =  ((n - a) / 2) + 1
    
    else:
      tiempo = ((a-1)/2)+1
    
    print(int(tiempo))