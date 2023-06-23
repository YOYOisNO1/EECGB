    m,n=map(int,input().split())
    
    a=map(int,input().split())
    
    b=map(int,input().split())
    
def f(x,y):
        if x[0]==y[0]:
            if x[1]!=y[1]:
                return x[0]
            else:
                return 0
    
        if x[1]==y[1]:
            if x[0]!=y[0]:
                return x[1]
            else:
                return 0
    
        
        if x[0]==y[1]:
            if x[1]!=y[0]:
                return x[0]
            else:
                return 0
    
        if x[1]==y[0]:
            if x[0]!=y[1]:
                return x[1]
            else:
                return 0
    
        return 0
    
    
    c=[]
    d=[]
    e=[]
    for i in range(0,len(a),2):
    
        c=c+[[a[i],a[i+1]]]
        
    for j in range(0,len(b),2):
        d=d+[[b[j],b[j+1]]]
    r=0
    ff=[]
    for i in range(len(c)):
        e=[]
        for j in range(len(d)):
            
            e=e+[f(c[i],d[j])]
        
        ff+=e
        k=0
        m=0
        for jj in range(len(e)):
            if e[jj]!=0 and e[jj]!=m:
                k+=1
                m=e[jj]        
        if k>1:
            r=-1
            break
    t=[]
    
    for i in range(len(ff)):
        if ff[i]!=0:
            t=t+[ff[i]]
    
    if r==-1:
        print -1
    elif len(set(t))>1:
        print 0
    
    else:
        print t[0]