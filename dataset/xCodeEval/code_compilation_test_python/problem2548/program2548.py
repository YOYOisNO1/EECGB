    
    import sys
    #sys.stdin=open("data.txt")
    input=sys.stdin.readline
    
def gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    
def modpow(x,y,m):
        # (x**y) % m
        if y==0: return 1%m
        elif y==1: return x%m
        elif y&1: return (modpow((x*x)%m,y//2,m)*x)%m
        else: return modpow((x*x)%m,y//2,m)
    
def inv(x,m):
        # return the inverse of x, modulo m
        # use euler's theorem
        tot=m
        mt=m
        for i in range(2,mt):
            if i*i>mt: break
            if mt%i==0:
                tot//=i
                tot*=i-1
                while mt%i==0: mt//=i
        if mt>1:
            tot//=mt
            tot*=mt-1
        # totient(m) = tot
        return modpow(x%m,tot-1,m)
    
def crt(x1,m1,x2,m2):
        # chinese remainder theorem solver
        # clean up
        m1=abs(m1)
        m2=abs(m2)
        x1%=m1
        x2%=m2
        if m1>m2:
            m1,m2=m2,m1
            x1,x2=x2,x1
        # get out a factor
        t=gcd(m1,m2)
        offset=x1%t
        if x1%t != x2%t:
            print("Something went wrong with the no intersection step")
        x1//=t
        m1//=t
        x2//=t
        m2//=t
        # get important numbers
        # r1 is 1 mod m1 and 0 mod m2
        # r2 is 0 mod m1 and 1 mod m2
        r1=(m2*inv(m2,m1))%(m1*m2)
        r2=(m1*inv(m1,m2))%(m1*m2)
        # pretty much done
        return t*((x1*r1+x2*r2)%(m1*m2))+offset
    
    # k',l'>=0 is the most annoying thing ever
    a1,b1,a2,b2,l,r=map(int,input().split())
    
    # bound l,r so nothing breaks
    if a1>=0: l=max(l,b1)
    if a1<=0: r=min(r,b1)
    if a2>=0: l=max(l,b2)
    if a2<=0: r=min(r,b2)
    
    if l>r: print(0)
    elif l==r:
        # special case
        ans=1
        if b1!=l and (a1==0 or (l-b1)%a1 or (l-b1)//a1<0): ans=0
        if b2!=l and (a2==0 or (l-b2)%a2 or (l-b2)//a2<0): ans=0
        print(ans)
    elif (b1-b2)%gcd(a1,a2)!=0:
        # they don't intersect
        print(0)
    else:
        # general case is the best case
        a3=abs((a1*a2)//gcd(a1,a2))
        b3=crt(b1,a1,b2,a2)
        # solve stuff easily now
        # python rounds down always
        l=(l-b3+a3-1)//a3
        r=(r-b3)//a3
        print(max(0,r-l+1))