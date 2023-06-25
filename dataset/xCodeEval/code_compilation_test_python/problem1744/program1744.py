    m, n, k = map(int, input().split())
    mod = 10**9+7
def powermod(x,y):
      res = 1
      while(y>0):
        if y&1:
          res=res*x%mod
        x=x*x%mod
        y=y»1
      return res
    
    if (m%2 != n%2 and k == -1):
      print (0)
    else:
      print (powermod(2, (m-1)*(n-1)))