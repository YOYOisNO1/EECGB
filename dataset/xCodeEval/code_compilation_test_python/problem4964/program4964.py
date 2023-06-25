    
def readints():
      return map(int, input().split())
    
    
def dn(x):
      k=0
      t=x-1
      while t:
        t/=10
        k+=1
      return k
    
    
    
def _li(x, dn):
      ret=[]
      for _ in xrange(dn):
        ret.append(x%10)
        x/=10
      return ret
    
def li(h,m):
      return _li(h,dh)+_li(m,dm)
    
def dif(h1,m1,h2,m2):
      return sum(v1!=v2 for v1,v2 in zip(li(h1,m1), li(h2,m2)) )
    
    pow10=[10**i for i in xrange(12,-1,-1)]
    
    memo={}
    
def g(h,m):
      if (h,m) in memo:return memo[(h,m)]
      ret=f(0,1,h,m)+(1>=k)
      memo[(h,m)]=ret
      return ret
    
    
def f(h1,m1,h2,m2):
      if (h1,m1)==(h2, m2):ret = 0
      elif (h1,m1)>(h2,m2):
        ret = f(h1, m1, H-1, M-1) + f(0, 0, h2, m2) + ( dif(h1,m1,h2,m2) >= k)
      else:
        for hh in pow10:
          if (h1+hh, m1)<=(h2, m2) and h1/hh%10!=9:
            ret = g(hh,0)+f(h1+hh, m1, h2, m2)
            break
        else:
          for mm in pow10:
            if m1+mm<M and (h1,m1+mm)<=(h2,m2) and m1%mm%10!=9:
              ret = g(0,mm) + f(h1,m1+mm, h2, m2)
              break
          else:
            nt=h1*M+m1+1
            nh,nm=nt/M,nt%M
            ret = ( dif(h1,m1,nh,nm)>=k ) + f(nh,nm,h2,m2)
      #print h1,m1,h2,m2,ret
      return ret
    
def main():
      global H,M,k,dh,dm
      H,M,k=readints()
      h1,m1=readints()
      h2,m2=readints()
      """H,M,k=24,60,1
      h1,m1=0,0
      h2,m2=23,59
      H,M,k=24,60,3
      h1,m1=23,59
      h2,m2=23,59"""
      dh=dn(H)
      dm=dn(M)
      print f(h1,m1,h2,m2)
    
    main()