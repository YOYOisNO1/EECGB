    mp={0:[0,1],1:[1,1]}
def f1(nn):
        if nn not in mp.keys():
            x=nn/2
            y=nn%2
            retx=0
            rety=0
            if x in mp.keys():
                retx=mp[x]
            else:
                retx=f1(x)
                mp[x]=retx
            if y in mp.keys():
                rety=mp[y]
            else:
                rety=f1(y)
                mp[y]=rety
            
            mp[nn]=[retx[0]*2+rety[0],retx[1]*2+rety[1]]
        
        return mp[nn]
    
def f2(nn,ll,rr,ans):
        if ll==rr:
            return ll,ans
        
        if ll+mp[nn/2][1]<=rr:
            ll+=mp[nn/2][1]
            ans+=mp[nn/2][0]
        else:
            ll,ans=f2(nn/2,ll,rr,ans)
            
        if ll+mp[nn%2][1]<=rr:
            ll+=mp[nn%2][1]
            ans+=mp[nn%2][0]
        else:
            ll,ans=f2(nn%2,ll,rr,ans)
                
        if ll+mp[nn/2][1]<=rr:
            ll+=mp[nn/2][1]
            ans+=mp[nn/2][0]
        else:
            ll,ans=f2(nn/2,ll,rr,ans)
    
        return ll,ans;
    
    n,l,r=map(int,input().split())
    
    if n==1:
        print(1)
    else:
        f1(n)
        
        ansL=[0,0]
        ansR=[0,0]
        if l>1:
            ansL=f2(n,0,l-1,0)
        ansR=f2(n,0,r,0)
    
        print(ansR[1]-ansL[1])
    
    
    