    n,d,S=map(int,input().split())
    c0=[[0,0] for i in range(n)]
    c1=[[0,0] for i in range(n)]
    c2=1
    for i in range(n):
        c,f,l=map(int,input().split())
        c2+=c
        if c>0 : c1[i][0]=f;c1[i][1]=l;
        else : c0[i][0]=f;c0[i][1]=l;
    
def solc0(N,T):
        c0.sort()
        res=0
        ct=0
        for i in range(len(c0)):
            if c0[i][1]>=d:
                if res+c0[i][0]<=T and ct<N:
                    res+=c0[i][0]
                    ct+=1
                else:break;
        return ct,res
    
def solc1():
        c1.sort()
        res=-1
        for i in range(len(c1)):
            if c1[i][1]>=d:
                if c1[i][0]<=S:
                    res=c1[i][0]
                    c0.extend(c1[i+1:])
                else: return 0,0
        if res<0 : return 0,0
    
        tc,tr=solc0(n-c2,S-res)
        ct=tc+c2
        res+=tr
        return ct,res
    
    ct,res=solc0(n,S)
    ct2,res2=solc1()
    if ct<ct2 or (ct==ct2 and res>res2):
        ct,res=ct2,res2
    
    print ct,res
    