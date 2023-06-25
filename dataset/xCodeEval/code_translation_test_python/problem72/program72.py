    import math
def lcm(i,j):
      return i//math.gcd(i,j)*j
    
    n,m=map(int,input().split())
    
    c=[0]*20
    for bit in range(1,1<<20):
      bitcnt=0
      L=1
      mx=-1
      right=1<<30
      left=-1
      for i in range(20):
        if (bit>>i)&1:
          bitcnt+=1
          mx=i
          left=i+1
          right=min(right,m*(i+1))
          if L!=-1:
            L=lcm(L,i+1)
            if L>2**28:
              L=-1
      if L==-1:
        continue
      if bitcnt%2==1:
        c[mx]+=max(0,right//L-(left-1)//L)
      else:
        c[mx]-=max(0,right//L-(left-1)//L)
    
    for i in range(1,20):
      c[i]+=c[i-1]
    
    seen=[False]*(n+1)
    seen[1]=True
    ans=1
    
    for i in range(2,n+1):
      if seen[i]:continue
      tmp=1
      now=i
      seen[now]=True
      while now*i<=n:
        tmp+=1
        now*=i
        seen[now]=True
      
      ans+=c[tmp-1]
    
    print(ans)