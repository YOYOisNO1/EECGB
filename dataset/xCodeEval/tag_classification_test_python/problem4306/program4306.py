def program4306():
    w = [int(x) for x in input().split(' ')]
    b = [
      [int(x) for x in input().split(' ')],
      [int(x) for x in input().split(' ')]
    ]
    r = [0, 0, 0, 0]
    rot = []
    res = True
    for i in b:
      t = 0
      if i[2] >= w[0] >= i[0] and i[1] <= w[1] <= i[3] :#left bot
        r[0] = 1
        t += 1
      if i[2] >= w[0] >= i[0] and i[1] <= w[3] <= i[3] :#left top
        r[1] = 1                                                            
        t += 2
      if i[2] >= w[2] >= i[0] and i[1] <= w[3] <= i[3]:#right top
        r[2] = 1
        t += 4
      if i[2] >= w[2] >= i[0] and i[1] <= w[1] <= i[3]:#right bot
        r[3] = 1
        t += 8
      if t == 3:
        rot.append('left ver')
      elif t == 12:
        rot.append('right ver')
      elif t == 6:
        rot.append('top hor')
      elif t == 9:
        rot.append('bot hor')
      elif t in [7, 11, 13, 14, 15]:#should be fine with just 15 tho
        rot.append('cover')
    if r[0] and r[1] and r[2] and r[3]:
      if 'cover' in rot:
        res = False
      else:
        if 'ver' in rot[0] and 'ver' in rot[1]:
          if 'left' in rot[0] and b[1][0]-b[0][2]<=0:
            res = False
          if 'right' in rot[0] and b[0][0]-b[1][2]<=0:
            res = False
        if 'hor' in rot[0] and 'hor' in rot[1]:
          if 'top' in rot[0] and b[0][1]-b[1][3]<=0:
            res = False
          if 'bot' in rot[0] and b[1][1]-b[0][3]<=0:
            res = False
    if res:
      print('YES')
    else:
      print('NO')