def program3898():
    s,x1,x2=map(int,input().split())
    t1,t2=map(int,input().split())
    p,d=map(int,input().split())
    if t1>=t2:
        print(abs(x2-x1)*t2)
    else:
        if x1<x2:
            if p>x1 and d==-1:
                ans=(p-x1)*t1+x1*t1+x2*t1
            elif p<x1 and d==1:
                ans=(x2-p)*t1
            elif p<x1 and d==-1:
                ans=p*t1+x2*t1
            elif p>x1 and d==1:
                ans=(s-p)*t1+(s)*t1+x2*t1
        else:
            if p>x1 and d==-1:
                ans=(p-x2)*t1
            elif p<x1 and d==-1:
                ans=(p+s+s-x2)*t1
            elif p<x1 and d==1:
                ans=(s-p+s-x2)*t1
            elif p>x1 and d==1:
                ans=(2*s-p-x2)*t1
        print(min(ans,abs(x2-x1)*t2))