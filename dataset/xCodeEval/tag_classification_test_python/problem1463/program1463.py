def program1463():
    a, b, c = map(int, input().split())
    x = a+b-c
    y = b+c-a
    z = c+a-b
    if any((x&1,y&1,z&1,x<0,y<0,z<0)):
      print('Impossible')
    else:
      print(x//2, y//2, z//2)