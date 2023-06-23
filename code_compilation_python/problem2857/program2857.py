def program2857():
    in = input()
    x = int(in.split()[0])
    y = int(in.split()[1])
    l = int(in.split()[2])
    r = int(in.split()[3])
    b=set()
    a=0
    b.add(l-1)
    b.add(r+1)
    for i in range(100):
      xx=x**i
      if xx>r: break
      for j in range(100):
        rr=xx+(y**j)
        if rr>r: break
        if rr>=l:
          b.add(rr)
    b=sorted(list(b))
    for i in range(1,len(b)):
      a=max(a,b[i]-b[i-1]-1)
    print(a)