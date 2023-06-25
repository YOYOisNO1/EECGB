    from fractions import Fraction
    vp=Fraction(int(input()))
    vd=Fraction(int(input()))
    t=Fraction(int(input()))
    f=Fraction(int(input()))
    c=Fraction(int(input()))
    
    
def dogon(dist):
        X=(dist*vp)/(vd-vp)
        return dist+X
    if(vp>vd):
        print 0;
    else:
     curdist=Fraction(t*vp)
     count=0
     while True:
         nextdist=dogon(curdist)
         #print nextdist
         if(nextdist<c):
             count+=1
         else:break
         curdist=nextdist+nextdist/vd*vp+f*vp
     print count
          
          
         