def upw(a,b):
        if a>0: return (a+b-1)/b
        a=-a
        return -(a/b)
def dwn(a,b):
        if a>0:return a/b
        a=-a;
        return -( (a+b-1)/b )
def xgcd(a,b):
        if(b==0): return [a,1,0];
        g,x1,y1=xgcd(b,a%b)
        return [g,y1,x1-(a/b)*y1];
    
    a1,b1,a2,b2,l,r=map(long,input().split())
    if b2<b1:
        a1,a2=a2,a1
        b1,b2=b2,b1
    
    g,x,y=xgcd(a1,a2)
    if (b2-b1)%g!=0: print(0)
    else:
        x=x*( (b2-b1)/g )
        y=y*( (b2-b1)/g )
        li1=max(upw(-x*g,a2),upw(y*g,a1))
        li2=upw((l-a1*x-b1)*g,a1*a2)
        ls=dwn((r-a1*x-b1)*g,a1*a2)
        li=max(li1,li2)  
        if li>ls: print(0)
        else: print(ls-li+1)