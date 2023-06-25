def main():
      path = input()
      coordinate = [[0 for i in range(2)] for j in range(len(path)+1)]
      coordinate[0] = [0,0]
      left = 0
      right = 0
      up = 0
      down = 0
    
      for direction in path:
        if direction == 'U':
          up += 1
        elif direction == 'R':
         right += 1
        elif direction == 'D':
          down += 1
        elif direction == 'L':
          left += 1
    
      if (left = 1 and right = 1 and up = 1 and down = 0) or (left = 1 and right = 1 and up = 0 and down = 1) or (left = 1 and right = 0 and up = 1 and down = 1) or (left = 0 and right = 1 and up = 1 and down = 1):
          print('BUG')
          return
    
      for i in range(0,len(path)):
        if i == 0:
          if path[i] == 'U':
            coordinate[i + 1][0] = 0
            coordinate[i + 1][1] = 1
          elif path[i] == 'R':
            coordinate[i + 1][0] = 1
            coordinate[i + 1][1] = 0
          elif path[i] == 'D':
            coordinate[i + 1][0] = 0
            coordinate[i + 1][1] = -1
          elif path[i] == 'L':
            coordinate[i + 1][0] = -1
            coordinate[i + 1][1] = 0
        else:
          if path[i] == 'U':
            coordinate[i + 1][0] = coordinate[i][0]
            coordinate[i + 1][1] += 1 + coordinate[i][1]
          elif path[i] == 'R':
            coordinate[i + 1][1] = coordinate[i][1]
            coordinate[i + 1][0] += 1 + coordinate[i][0]
          elif path[i] == 'D':
            coordinate[i + 1][0] = coordinate[i][0]
            coordinate[i + 1][1] += -1 + coordinate[i][1]
          elif path[i] == 'L':
            coordinate[i + 1][1] = coordinate[i][1]
            coordinate[i + 1][0] += -1 + coordinate[i][0]
      coordinateSet = list(set(map(tuple,coordinate)))
      if len(coordinate) == len(coordinateSet):
        print('OK')
      else:
        print('BUG')
    
    main()