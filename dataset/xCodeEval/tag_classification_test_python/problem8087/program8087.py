def Solve(x,y,c):
        if(c==len(virus)):
            return 0
        if(x==len(s1) or y==len(s2)):
            return ""
        if((x,y,c) in Mem):
            return Mem[(x,y,c)]
        ans=""
        if(s1[x]==s2[y]):
            q=0
            if(s1[x]==virus[c]):
                q=Solve(x+1,y+1,c+1)
                if(q!=0):
                    q=s1[x]+q
            else:
                done=False
                for match in T[c]:
                    if(s1[x]==virus[match]):
                        done=True
                        q=Solve(x+1,y+1,match+1)
                        if(q!=0):
                            q=s1[x]+q
                        break
                if(not done):
                    q=Solve(x+1,y+1,0)
                    if(q!=0):
                        q=s1[x]+q
            if(q!=0):
                ans=q
        q=Solve(x+1,y,c)
        if(q!=0):
            ans=max(ans,Solve(x+1,y,c),key=len)
        q=Solve(x,y+1,c)
        if(q!=0):
            ans=max(ans,Solve(x,y+1,c),key=len)
        Mem[(x,y,c)]=ans
        return ans
    
    Mem={}
    s1=input()
    s2=input()
    virus=input()
    
    T=[0]*len(virus)
    T[0]=[0]
    
    for i in range(1,len(virus)):
        done=False
        T[i]=[]
        for j in range(1,i):
            if(virus[j:i]==virus[:i-j]):
                T[i].append(i-j)
        T[i].append(0)
    
    e=Solve(0,0,0)
    if(e==""):
        print(0)
    else:
        print(Solve(0,0,0))