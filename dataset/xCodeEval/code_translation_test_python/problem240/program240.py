def program240():
    a, b, c = map(int, input().split(' '))
    
    x = a+b-c
    y = -a+b+c
    z = a-b+c
    
    works = True
    for i in [x, y, z]:
      if i%2 != 0 or i < 0:
        works = False
    
    if works:
      print(x/2,) y/2, z/2
    else:
      print('Impossible')