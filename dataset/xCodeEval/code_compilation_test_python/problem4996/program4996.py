    import fileinput
    
    input = fileinput.input()
def readstr():
      return input.readline().rstrip()
    
def readints():
      return [int(x) for x in readstr().split(' ')]
    
def sign(n):
      return 1-(n&1)*2
    
def coeffs(d,p):
      inv = [1]*(d+1)
      for i in xrange(2,d+1):
        inv[i] = (-(p/i)*inv[p%i])%p
      finv = [1]*(d+1)
      for i in xrange(d):
        finv[i+1]=(finv[i]*inv[i+1])%p
      sumd=d*(d+1)/2
      sumd2=d*(d+1)*(2*d+1)/6
      return [(inv[d]*inv[d-1]*sign(d-j)*((sumd-j)**2-sumd2+(j**2))*finv[j]*finv[d-j])%p for j in xrange(d+1)]
    
    # cell[z]=cell[x]+cell[y]
def plus(x,y,z):
      print '+ {} {} {}'.format(x,y,z)
    
    # cell[y]=cell[x]^d
def powd(x,y):
      print '^ {} {}'.format(x,y)
    
def output(x):
      print 'f {}'.format(x)
    
    # cell[y]+=k*cell[x]
    # Modifies cell[x]
def kplus(k,x,y):
      k=k%p
      while k:
        if k&1: plus(x,y,y)
        k/=2
        plus(x,x,x)
    
    # cell[y]+=k*cell[x]^2
    # Requires c=coeffs(d,p) and cell[one]==1
    # Modifies cell[x] and cell[z]
def ksquare(k,x,y,c,one,tmp):
      for j in xrange(d+1):
        if j: plus(x,one,x)
        powd(x,tmp)
        kplus(c[j]*k,tmp,y)
    
    # x, y, x+y, 1, result, tmp
    d,p = readints()
    c=coeffs(d,p)
    half=(p+1)/2
    plus(1,2,3)
    kplus(-1,6,5)
    ksquare(-half,1,5,c,4,6)
    ksquare(-half,2,5,c,4,6)
    ksquare(half,3,5,c,4,6)
    output(5)
    
def test(d,p):
      c=coeffs(d,p)
      for x in xrange(1000):
        assert pow(x,2,p)==sum(pow(x+j,d,p)*cj for j,cj in enumerate(c))%p