def program430():
    inp=input()
    L=[]
    s=""
    x=len(inp)
    if x%2==1:
      for i in range(len(inp)):
       if i%2==0:
        L.append(inp[(1)*(i/2+1)-1])
    
       else:
        L.append(inp[(-1)*(i/2+1)])
    else:
      for i in range(len(inp)):
       if i%2==0:
        L.append(inp[(-1)*(i/2+1)])
    
       else:
        L.append(inp[(i/2+1)-1])
    for i in range(len(L)):
      s+=L[-i-1]
    print(s)
    """
    0 1 1
    2 3 2
    4 5 3
    6 7 4"""