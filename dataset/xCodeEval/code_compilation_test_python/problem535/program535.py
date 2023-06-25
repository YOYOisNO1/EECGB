def program535():
    a, b, c = map(int, input().split())
    x = a+b-c
    y = b+c-a
    z = c+a-b
    if x&1 or y&1 or z&1 or x<0 or y<0 or z<0:
      print('IMPOSSIBLE')
    else
      print(x//2, y//2, z//2)a, b, c = map(int, input().split())
    x = a+b-c
    y = b+c-a
    z = c+a-b
    if x&1 or y&1 or z&1 or x<0 or y<0 or z<0:
      print('Impossible')
    else:
      print(x//2, y//2, z//2)