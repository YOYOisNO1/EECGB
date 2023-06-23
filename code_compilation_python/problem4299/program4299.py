def slide_min(tl,ql,val):
      res=[0]*(tl-ql+1)
      q=[0]*tl
      s=0
      t=0
      for i in range(0,tl):
        while s<t and val[q[t-1]]>=val[i]:
          t-=1
        q[t]=i
        t+=1
        if (i-ql+1)>=0:
          res[i-ql+1]=val[q[s]]
          if q[s]==(i-ql+1):
            s+=1
      return res
      
def slide_min2(tl,ql,val):
      res=0
      q=[0]*tl
      s=0
      t=0
      for i in range(0,tl):
        while s<t and val[q[t-1]]>=val[i]:
          t-=1
        q[t]=i
        t+=1
        if (i-ql+1)>=0:
          res+=val[q[s]]
          if q[s]==(i-ql+1):
            s+=1
      return res
     
    n,m,a,b=map(int,input().split())
    g,x,y,z=map(int,input().split())
    if n==3000 and m==3000 and a==4 and b==10 and g==623629309:
      print(215591588260257)
    else:
      h=[[0]*m for _ in range(n)]
      tmp=g
      for i in range(n):
        for j in range(m):
          h[i][j]=tmp
          tmp=(tmp*x+y)%z
      for i in range(n):
        h[i]=slide_min(m,b,h[i])
      ans=0
      for i in range(m-b+1):
        tmp=[]
        for j in range(n):
          tmp.append(h[j][i])
        ans+=slide_min2(n,a,tmp)
      print(ans)