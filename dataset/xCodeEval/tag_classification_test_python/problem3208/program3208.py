    from sys import stdin
def gcd(a,b):
     while a%b:
      t=a%b;a=b;b=t
     return b
def su(x,y):
     r = 0
     while x:
      r+=x%y;x/=y
     return r
    n = int(stdin.readline())
    fir,sec = 0,0
    for j in xrange(2,n):
     sec+=1
     fir+=su(n,j)
    g = gcd(fir,sec)
    fir/=g
    sec/=g
    print(str(fir)) + "/" + str(sec)
     