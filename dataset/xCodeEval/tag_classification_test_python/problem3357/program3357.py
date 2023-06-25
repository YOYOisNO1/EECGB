    n,s=map(int,input().split())
    l=0
    u=10**22
def sod(n):
      st=str(n)
      v=0
      for i in st:
        v=v+int(i) 
      return v  
    
    for i in range(1,200):
      m=(l+u)/2
      if m>=sod(m)+s:
        u=m 
      else:
        l=m 
      #print(l,u,m)
    #print(l,u)
    if sod(l)>=sod(l)+s:
      print(max(n-l+1,0)) 
    else:
      print(max(n-u+1,0))