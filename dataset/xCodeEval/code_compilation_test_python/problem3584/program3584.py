def binary_gcd(a,b):
        d=0
        while a%2==0 and b%2==0:
            a=a//2
            b=b//2
            d+=1
        while a!=b:
            if a%2==0:
                a=a//2
            elif b%2==0:
                b=b//2
            else:
                if a>b:
                    a=(a-b)//2
                else:
                    b=(b-a)//2
        g=a
        return g*2**d
def check_aval(n):
        f=0
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                f=i
                break
        return f
    a,b=map(int,input().split())
    i=0
    if check_aval(a)==0 or b==1:
        if(b%a!=0  or a==1 or b==1):
            if a>b:
                i=b
            else:
                i=b%a+b//a
            b=0
    ##    elif b>a:
    ##        i=b%a+b//a
    ##        b=0
    gcd=1
    ar=[]
    while  b!=0 and :
        try:
            if gcd==1:
                gcd=binary_gcd(a,b)
            else:
                gcd=gcd*binary_gcd(a//gcd,(b-gcd)//gcd)
            b-=gcd
            i+=1
            if b!=0:
                if check_aval((b-gcd)//gcd)==0:
                    i+=b//gcd
                    #b=0
                    ar.append(i)
                    i-=b//gcd
        except:
            i-=1
            gcd=binary_gcd(a,b)
            b-=gcd
            i+=1
    ##        b-=gcd
    ##        i+=1
    ##    else:
    ##        b-=gcd
    ##        i+=1
    #print(i)
    print(min(ar))
    