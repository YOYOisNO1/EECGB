def program1501():
    l1,r1,l2,r2,k = map(int,input().split())
     
    lm = max(l1,l2)
    rm = min(r1,r2)
     
    if lm > rm:
      print(0)
     
    elif lm <= k <= rm:
      print(rm-lm)
    else:
      print(rm-lm+1)