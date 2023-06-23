def gcd(a,b):
      if b==0: return a
      else return gcd(b,a%b)
    a,b=map(int,input().split())
    d=gcd(a,b)
    a/=d
    b/=d
    if b==a+1 or b+1==a: print 'Equal'
    if a>b: print 'Masha'
    if a<b: print 'Dasha'