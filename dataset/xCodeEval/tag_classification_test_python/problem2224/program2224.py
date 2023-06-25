    grid = []
    
    for count in range(11):
      i = input().replace(" ", "")
      if (i == ""):
        continue
      grid += [list(i)]
    #  print(i)
    x, y = list(map(int, input().split()))
    #print(x,y)
    x -= 1
    y -= 1
    #print(x,y)
    
    #print()
    
def show(ar):
      s = ""
      for counter in range(1, 10):
        s += ar[counter-1]
        if counter%3 == 0:
          s += " "
      print(s)
    '''
    for a in grid:
      show(a)
    '''
    x = (x%3)*3
    y = (y%3)*3
    #print(x,y)
    
    tot = 0
    for i in range(x, x+3):
      for j in range(y, y+3):
        if grid[i][j] == ".":
          grid[i][j] = "!"
          tot += 1
    
    if (tot == 0):
      for i in range(9):
        for j in range(9):
          if grid[i][j] == ".":
            grid[i][j] = "!"
    
    for a in range(9):
      row = grid[a]
      show(row)
      if a%3 == 2:
        print()