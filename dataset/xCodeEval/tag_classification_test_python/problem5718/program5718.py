    import math
    
def test(a,b):
      global ss,sj
      if abs((X*b-Y*a)*sj)<abs((X*sj-Y*ss)*b):
        ss=a
        sj=b
    
def solve(b):
      a=math.floor(X*b/Y)
      test(a,b)
      a+=1
      test(a,b)
    
    X,Y,N = map(int,input().split())
    ss=0
    sj=1
    for i in xrange(1,N+1):
      solve(i)
    print("%d/%d") % (ss,sj)
    