def program4296():
    s=input()
    s=list(s)
    k=int(input())
    c=int(0)
    cstar=int(0)
    cque=int(0)
    ans=[]
    for i in range(0,len(s)):
        if(s[i]!='*' and s[i]!='?'):
            c=c+1
            ans.append(s[i])
        if(s[i]=='*'):
            cstar+=1
        if(s[i]=='?'):
            cque+=1
    if(c==k):
        ans=''.join(ans)
        print(ans)
    elif(c<k):
        diff=k-c
        if(cstar>0):
            ans=[]
            for i in range(len(s)-1,-1,-1):
                if(s[i]=='*'):
                    d=s[i-1]
                    t=s[:i]
                    td=s[i+1:]
                    rep=d*diff
                    rep=list(rep)
                    ans=t+rep+td
                    break
            ans1=[]    
            for i in range(0,len(ans)):
                if(ans[i]!='*' and ans[i]!='?'):
                    ans1.append(ans[i])
            ans1=''.join(ans1)    
            print(ans1)   
        else:
            print("Impossible")
    else:
        ans1=[]
        if((c-k)<=(cque+cstar)):
            diff=(c-k)
            for i in range(0,len(s)-1):
                if(diff>0):
                    if(s[i]!='*' and s[i]!='?'):
                        if(s[i+1]=='*' or s[i+1]=='?'):
                            diff-=1
                        else:
                            ans1.append(s[i])
                else:
                    if(s[i]!='*' and s[i]!='?'):
                        ans1.append(s[i])
            if(s[len(s)-1]!='*' and s[len(s)-1]!='?'):
                ans1.append(s[len(s)-1])
            ans1=''.join(ans1)
            print(ans1)
        else:
            print("Impossible")
        
        