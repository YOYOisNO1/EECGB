def program2285():
    st = map(int,input(""))
    ot = "NO"
    for x,y in enumerate(st):
      sm = sum(st[x:x+7])
      if len(st[x:x+7]) ==7 and(sm == 0 or sm ==7):
        ot = "YES"
        break
    print(ot)