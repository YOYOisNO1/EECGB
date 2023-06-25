    import sys, os
     
    if os.environ['USERNAME']=='kissz':
        s='4897332836602749275099151826428737446171648588383'
        #s='34035589464304102353337687153068150731986217146'
        #s='102'
        #s='9105539'
    def debug(*args):
            print(*args,file=sys.stderr)
            sys.stderr.flush()
    else:
        s=input().strip()
    def debug(*args):
            pass
     
    # SCRIPT STARTS HERE
     
def sub(x,y):
        n=len(x)
        m=len(y)
        assert(n==m)
        z=[0]*n
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
        return z
     
    x0=[int(c) for c in s]
    while x0[0]==0: x0.pop(0)
    x0=[0]+x0
    n=len(x0)
    o=0
    best=1<<30
    
    
    visit=0
    Q=[(0,n,x0)]
    while Q:
        r,l,x=Q.pop()
        visit+=1
        if l==0:
            debug(best,len(Q),visit)
            continue
        if r>=best:
            continue
        zlim=9
        for a in range(x[0]-1,x[0]+2):
            z=sub([a]*l,x)
            if l==1 and z[0]==0:
                best=min(best,r+a)
            elif z[0]==0 and z[1]<=zlim:
                zlim=z[1]
                Q.append((r+a*l,l-1,z[1:]))
    debug(visit)
    print(best)