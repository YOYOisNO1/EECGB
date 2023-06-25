def program436():
    from fractions import *
    n=int(input())
    a,ans,last=Fraction(1,n),Fraction(0,1),-1
    for i in range(n):
        t=Fraction(1,2**i)
        if (t<=a):
            a-=t
            ans+=i*t
            if (a.numerator==1):
                if (last>=0):
                    d=i-last
                    break
                res,last=ans,i
    res=(res*n+Fraction(d,2**d))/(1-Fraction(1,2**d))
    print(res,end='')
    if (res.denominator==1):print('/1')
    print('')