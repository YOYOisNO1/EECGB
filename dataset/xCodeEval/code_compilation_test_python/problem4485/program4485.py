def program4485():
    import random
    import sys
    random.seed(12345)
    
    n, m = map(int, input().split())
    bad = set([tuple(map(int, input().split())) for _ in range(m)])
    items = range(1, n+1)
    
    for _ in range(100000):
      random.shuffle(items)
      fail = False
      for i in range(m):
        if (items[i], items[i-1]) in bad or (items[i-1], items[i]) in bad:
          fail = True
          break
      if not fail:
        for i in range(m):
          print items[i], items[i-1]
        sys.exit(0)
    
    print -1