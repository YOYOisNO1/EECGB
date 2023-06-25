def program1327():
    n,k,m,d=map(int,input().split())
    if d==1:
      print(m) 
    else:
      lst=[m]
      for i in range(1,d+1):
        vr=(i-1)*(k-1)+(i)
        #print(vr,n/vr,(n/vr)*i)
        if 1==1:
          lst.append((min(m,n/vr))*(i))
          #break
      #print(lst)
      print(max(lst))