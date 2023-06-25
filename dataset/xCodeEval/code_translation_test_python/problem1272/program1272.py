def program1272():
    from fractions import Fraction
    a,b,c,d=map(int,input().split())
    # if(max(a,b)<max(c,d)):
    #     z=Fraction(Fraction(a,b),Fraction(c,d))
    # else:
    #     z=Fraction(Fraction(c,d),Fraction(a,b))
    
    # if((Fraction(1,1)-z)==0):
    #     print("0/1")
    # else:
    #     print(Fraction(1,1)-z)
                   
    z1=Fraction(Fraction(a,b),Fraction(c,d))
    z2=Fraction(Fraction(c,d),Fraction(a,b))
    
    if((Fraction(1,1)-z1)==0):
        print("0/1")
        
    else:
        x=Fraction(1,1)-z1
        if(x>0 and x<1):
            print(x)
        else:
            print(Fraction(1,1)-z2)