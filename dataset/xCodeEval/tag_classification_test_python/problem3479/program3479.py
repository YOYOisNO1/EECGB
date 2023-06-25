def gcd(a,b):
        while(a>0 and b>0):
            if(a>b):
                a%=b
            else:
                b%=a
        return max(a,b)
    t,b,w=map(int,input().split())
    k=b*w/gcd(b,w)
    tt=t/k
    no=min(b,w)-1
    tot=no*tt
    tot+=min(t-tt*k,no)+tt
    g=gcd(t,tot)
    n1=tot/g
    n2=t/g
    print("%d/%d")%(n1,n2)