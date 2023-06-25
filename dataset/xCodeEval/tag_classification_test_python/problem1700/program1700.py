def program1700():
    for i in [*open(0)][1:]:
     k = int(i)/100
     r = 1
     while True:
      n = round(r/k,2)
      if str(n)[-1] == '0':
       print(int(n))
       break
      else:
       r+=1