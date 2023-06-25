def program4516():
    n = int(input())
    a = input().split(' ')
    for i in range(0,len(a)):
      a[i] = int(a[i])
    
    cnt = 0
    
    while len(a) > 0:
      a.sort()
      f = a[0]
      b = []
      l = False
      for i in range(0,len(a)):
        if(a[i] % f != 0):
          b.append(a[i])
          l = True
      
      cnt += 1
      a = b
    
    print(cnt)