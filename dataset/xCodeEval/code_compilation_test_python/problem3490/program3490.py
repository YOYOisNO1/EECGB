def program3490():
    import math
    n= float (input("N: "))
    m= float (input("M: "))
    k= float (input("K: "))
    r=1.0
    d=1
    s=" "
    if (k%2==0):
        s="R"
        r = math.ceil((k/2)/m)
        if((k/2)%m==0):
         d=m
        else :
         d=(k/2)%m
    else:
        s="L"
        r = math.ceil(((k+1)/2)/m)
        if(((k+1)/2)%m==0):
         d=m
        else :
         d=((k+1)/2)%m
    
    print (str(r)+" "+str(int(d))+" "+s