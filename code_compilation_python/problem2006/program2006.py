def program2006():
    import sys
    import time
    sleep(1)
    for line in sys.stdin:
      vec  = line.split()
      val = [int(x) for x in vec[1:]].sort()
      print ' '.join(val)