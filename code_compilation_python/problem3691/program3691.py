    import sys, os
    
    if os.environ['USERNAME']=='kissz':
        s='102'
    def debug(*args):
            print(*args,file=sys.stderr)
    else:
        s=input().strip()
    def debug(*args):
            pass
    
    # SCRIPT STARTS HERE
    
def sub(x,y):
        n=len(x)
        m=len(y)
        x=[0]*(m-n)+x
        y=[0]*(n-m)+y
        z=[0]*max(n,m)
        greater=0
        for a,b in zip(x,y):
            if a>b:
                greater=1
                break
            elif a<b:
                greater=-1
                break
        if greater==0:
            return z
        elif greater==-1:
            x,y=y,x
        c=0
        for i in range(max(n,m)-1,-1,-1):
            a,b=x[i],y[i]
            b=b+c
            z[i]=(a-b)%10
            c=(a<b)
        startindex=0
        while z[startindex]==0: startindex+=1
        return z[startindex:]
    
    x=[int(c) for c in s]
    while x[0]==0: x.pop(0)
    n=len(x)
    o=0
    
def calc(x,flipped):
        if not x or sum(x)==0:
            return 0
        else:
            y1=[x[0]]*len(x)
            z1=sub(x,y1)
            if not flipped and sum(x)>len(x):
                y2=[1]*(len(x)+1)
                z2=sub(y2,[0]+x)
                return min(len(x)*x[0]+calc(z1,False),len(x)+1+calc(z2,True))
            else:
                return len(x)*x[0]+calc(z1,False)
    print(calc(x,False))