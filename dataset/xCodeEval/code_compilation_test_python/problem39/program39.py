def program39():
    import sys
    import time
    
    for line in sys.stdin:
      time.sleep(1.5)
      vec  = line.split()
      val = [str(y) for y in sorted([int(x) for x in vec[1:]])]
      print(' '.join(val))