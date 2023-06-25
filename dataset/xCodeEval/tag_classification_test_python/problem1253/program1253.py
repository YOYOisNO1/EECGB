def readarray(f): return map(f, input().split())
def readint(): return int(input())
def printlist(l): print(' ').join(map(str, l))
    
    n = readint()
    
    f = False
    c1 = 0
    c2 = 0
    for i in range(n):
      x, y = readarray(int)
      if x%2 != y%2:
        f = True
      c1 += x
      c2 += y
    c1 %= 2
    c2 %= 2
    
    if c1 == 0 and c2 == 0:
      print(0)
    elif c1 == 0 or c2 == 0:
      print(-1)
    elif f:
      print(1)
    else:
      print(-1)