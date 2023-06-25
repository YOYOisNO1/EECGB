    n,l,r=map(int,input().split())
    b=[]
    w=[1]
    while n:
      b+=n%2,
      w+=w[-1]*2+1,
      n/=2
    if not b:
      b+=0,
      w+=1,
    c=b[:]
    k=len(c)-1
    while k:
      c[k-1]=c[k]*2+b[k-1]
      k-=1
def go(p,i):
      if p<1:
        return 0
      if p>=w[-2-i]:
        return c[i]
      if p>w[-3-i]:
        return c[i]-go(w[-2-i]-p,i+1)
      return go(p,i+1)
    print(go(r,0)-go(l-1,0))