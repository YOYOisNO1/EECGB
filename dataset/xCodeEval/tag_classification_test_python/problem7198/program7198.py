    import sys
    
    try:
        f = open("input.txt", "r")
        sys.stdin = f
    except:
        pass
    
def readArray():
      return map(int, input().split())
    
    x1, y1 = readArray()
    x2, y2 = readArray()
    x3, y3 = readArray()
    
    acx, acy = x3 - x1, y3 - y1
    abx, aby = x2 - x1, y2 - y1
    
    cp = acx * aby - acy * abx
    
    if cp == 0:
      print("TOWARDS")
    elif cp > 0:
      print("RIGHT")
    else:
      print("LEFT")